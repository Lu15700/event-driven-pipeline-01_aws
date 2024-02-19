## Description
A pipeline on AWS to transform a CSV file to a Parquet file, once the CSV file is uploaded to the landing directory. Then, the transformed file is moved to a next stage directory, and the input file is changed to a better storage class.

## Technologies
- Python
- AWS SDK for Pandas
- AWS Lambda
- Amazon S3
- Amazon EventBridge

## Architecture
![architecture](https://github.com/Lu15700/event-driven-pipeline_in_aws/assets/102251361/4d100087-f1c8-491b-a7f3-21e901bca0f7)

## Snippet
![snippet](https://github.com/Lu15700/event-driven_pipeline_in_aws/assets/102251361/bff14695-4b79-4475-9d6e-43930ae457ac)

## Result
