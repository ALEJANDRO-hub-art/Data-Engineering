import boto3
import os
from datetime import datetime

s3 = boto3.client("s3")
sns = boto3.client("sns")

BUCKET_NAME = os.environ["BUCKET_NAME"]
PREFIX = os.environ.get("PREFIX", "raw/")
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

def lambda_handler(event, context):
    today = datetime.now().strftime("%Y-%m-%d")
    expected_file = f"{PREFIX}transactions_{today}.json"

    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=expected_file)
        return {
            "statusCode": 200,
            "body": f"File exists: {expected_file}"
        }
    except Exception:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Missing Daily Transaction File",
            Message=f"Expected file not found: s3://{BUCKET_NAME}/{expected_file}"
        )
        return {
            "statusCode": 404,
            "body": f"Missing file: {expected_file}"
        }
