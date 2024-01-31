import awswrangler as wr

def lambda_handler(event, context):
    
    # Key
    key = event['detail']['object']['key'].strip('input/ .csv')
    print('Key: ' + key)
    
    # Bucket, Prefixes, and Paths
    bucket = 'event-driven-pipeline-01-bucket'
    input_prefix = 'input'
    output_prefix = 'output'
    
    input_path = f"s3://{bucket}/{input_prefix}/"
    output_path = f"s3://{bucket}/{output_prefix}/{key}.parquet"
    
    # Data Frame Reading
    input_df = wr.s3.read_csv(path= input_path)
    
    # Data Transformation
    # TODO: To be implemented per requirements.
    
    # Data Format Conversion and Object Storage
    wr.s3.to_parquet(df= input_df, path= output_path)