private static void sendChurnData(ChurnData churn, KinesisAsyncClient kinesisClient, String streamName) {
	byte[] bytes = churn.toJsonAsBytes();
	if (bytes == null) {
		LOG.warn("Could not get JSON bytes for churn data");
		return;
	}
	LOG.info("Putting churn:" + churn.toString());
	PutRecordRequest request = PutRecordRequest.builder()
		.partitionKey(churn.getCustomerID())
		.streamName(streamName)
		.data(SdkBytes.fromByteArray(bytes))
		.build();

	try {
		kinesisClient.putRecord(request).get();
	} catch (InterruptedException e) {
		LOG.info("Interrupted, assuming shutdown.");
	} catch (ExecutionException e) {
		LOG.error("Exception while sending data to Kinesis. Will try again next cycle.", e);
	}

}