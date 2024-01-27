import os.path
import json
import time
import boto3

"""
send_churn_data: sends the json format data to kinesis
stream_name: Kinesis stream name
json_file_template: the template name/path for all json files
wait_time: sleep time to simulate streaming data
max_iter: safe-guarding while loop, feel free to change to fit larger data
"""
def send_churn_data(stream_name, json_file_template, wait_time=0.1, max_iter=10000):
	client=boto3.client('kinesis')
	counter=0
	while counter < max_iter:
		json_file_name = json_file_template + str(counter) + ".json"
		
		if not os.path.isfile(json_file_name):
			print("SEND DONE: Reached end of all files")
			break

		try:
			with open(json_file_name, encoding='utf-8') as jsonf:
				churn = json.load(jsonf)
		except Exception as err:
			print("could not read from:", json_file_name)
			print(err)
			counter+=1
			continue

		response = client.put_record(
			StreamName = stream_name,
			Data = json.dumps(churn),
			PartitionKey = str(hash(churn['customerID']))
			)

		if response['ResponseMetadata']['HTTPStatusCode'] != 200:
			print('Error!')
			print(response)
		else:
			print("Successfully sent churn_data #", counter)

		counter+=1
		time.sleep(wait_time)

	print("Send Churn Data finished.")

stream_name = "check-churn-kinesis-data-stream"
json_file_template = "./data/json/customer_churn_"
send_churn_data(stream_name, json_file_template)
