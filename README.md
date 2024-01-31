## Description
This a simple data processing pipeline that listens to certain events from an AWS S3 standard bucket prefix and triggers an AWS Lambda function to transform data, convert the file format from CSV to Parquet, and store the file back in a distinct AWS S3 standard bucket prefix. Furthermore, the input files are archived to a better storage class after they're processed.

## Architecture
