import boto3
import pandas as pd
import io
import json
from statistics import mean, mode, median

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # S3 bucket and file details
    bucket_name = 'quantum-kmeans-bucket'  # Change this to your S3 bucket name
    input_file_key = 'ghcnd-stations.csv'  # Change this to the correct file name in S3
    output_file_key = 'processed_output.csv'
    
    # Read the CSV file from S3
    response = s3.get_object(Bucket=bucket_name, Key=input_file_key)
    df = pd.read_csv(io.BytesIO(response['Body'].read()))
    
    # Data Analysis
    analysis_results = {}
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:  # Numeric columns
            analysis_results[col] = {
                'Mean': mean(df[col]),
                'Median': median(df[col]),
                'Mode': mode(df[col]) if len(df[col].unique()) > 1 else "No mode"
            }
        else:  # Non-numeric columns
            analysis_results[col] = {
                'Datatype': str(df[col].dtype)
            }
    
    # Sort alphabetically by first column (Assuming first column is categorical)
    df = df.sort_values(by=df.columns[0])
    
    # Save processed CSV to S3
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=bucket_name, Key=output_file_key, Body=csv_buffer.getvalue())
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'CSV file processed and uploaded to S3',
            'analysis_results': analysis_results,
            'processed_file': f's3://{bucket_name}/{output_file_key}'
        })
    }