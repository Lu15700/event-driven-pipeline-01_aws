## Description
TODO

This a simple data processing pipeline that listens to certain events from an AWS S3 standard bucket prefix and triggers an AWS Lambda function to transform data, convert the file format from CSV to Parquet, and store the file back in a distinct AWS S3 standard bucket prefix. Furthermore, the input files are archived to a better storage class after they're processed.

## Architecture
TODO

## Prefixes of S3 Bucket
![Prefixes of S3 Bucket](https://github.com/Lu15700/event-driven-pipeline-01_aws/assets/102251361/7276a758-04ab-40a9-8775-08e1314909e8)

## S3 Event Pattern for EventBridge Rule
![S3 Event Pattern for EventBridge Rule](https://github.com/Lu15700/event-driven-pipeline-01_aws/assets/102251361/350e0260-22c6-4d5f-928f-ed6844060593)
