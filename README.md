Creating a ML model with real-time data using AWS SageMaker, Kinesis, and S3

- Big Data has become part of our lives. Along with it came the increase in supply of many highly accurate Artificial Intelligence models, which use existing data to generate new data or classify, predict, or estimate existing data. As such, many companies have also shown interest in integrating AI into their applications and company tech stack. With this project, we explore how a company with continuous data stream can utilize Amazon Web Services systems such as Kinesis Data Streams, S3, and SageMaker to create an end-to-end Machine Learning pipeline, starting from data transfer-compilation until model prediction and analysis.
- In this paper, we’ve managed to gather 7000+ user churn data in separate JSON files through Kinesis Data Streams into S3, pre-process with PySpark, further pre-process with Data Wrangler, and build an ML model with SageMaker. Using the quick-build option, we were able to get a classification model within ten minutes (build time) with an overall 76% accuracy, and an F-score of 0.642, without having to tweak hyperparameters or define the type of ML model.
- The main purpose of this paper is to show how we approached the problem, the AWS architecture we came up with, and how the AWS systems make this convenient. Model accuracy is not a metric for this project.
- End-to-end Architecture: AWS CLI (JSON Streaming Data) -> AWS Kinesis Data Streams -> AWS Data Firehose -> AWS S3 -> AWS EMR-Spark -> AWS S3 -> AWS Data Wrangler -> AWS SageMaker

Useful Resources
- AWS Command Line Interface (CLI) Setup: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- AWS Command Line Interface (CLI) Configuration: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
- AWS Command Line Interface (CLI) Configuration-2: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html
- AWS Command Line Interface (CLI) - SSO Session: https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html
- AWS CLI Configuration - IAM Credentials tutorial: https://www.youtube.com/watch?v=BzzCIsjrE7U
- Convert CSV to JSON - Starter code for our parsing implementation: https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
- Send Data to Kinesis: https://github.com/ev2900/Flink_Kinesis_Data_Analytics/blob/main/kinesis_data_producer/NycTaxi_Producer_Desktop_JSON.py
- AWS SageMaker Documentation: https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html
