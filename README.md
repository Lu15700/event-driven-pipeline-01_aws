## Description
A pipeline in AWS to transform a CSV file to a Parquet file, once the CSV file is uploaded to the input directory. Then, the transformed file is moved to the output directory, and the input file is changed to [intelligent-tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) after 3 days.

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

### Input
![input](https://github.com/Lu15700/event-driven_pipeline_in_aws/assets/102251361/49023077-0c41-48d8-8591-f142f18318d8)

### Output
![output](https://github.com/Lu15700/event-driven_pipeline_in_aws/assets/102251361/febef3e0-a601-4d73-98bd-0f93cc4184e1)
