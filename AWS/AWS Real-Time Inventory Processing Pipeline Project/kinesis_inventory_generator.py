import datetime
import json
import boto3
import random
import time
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Create Kinesis client
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

event_types = [
    'product_added',
    'product_removed',
    'product_quantity_changed'
]

def random_timestamp(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    random_datetime = datetime.datetime(year, month, day, hour, minute, second)
    return random_datetime.isoformat()

def generate_inventory_data():
    event_type = random.choice(event_types)
    product_id = 'P' + str(random.randint(1, 10000))
    product_name = random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'])
    quantity = random.randint(1, 50)

    return {
        "event_type": event_type,
        "product": {
            "product_id": product_id,
            "product_name": product_name,
            "quantity": quantity,
            "timestamp": random_timestamp(2022, 2023)
        }
    }

if __name__ == '__main__':
    try:
        while True:
            data = generate_inventory_data()
            print("Generated data:", data)

            data_str = json.dumps(data)
            data_bytes = data_str.encode('utf-8')
            partition_key = data['product']['product_id']

            response = kinesis_client.put_record(
                StreamName='realtimeInventoryProcessing',
                Data=data_bytes,
                PartitionKey=partition_key
            )

            print("Record sent successfully:", response)
            time.sleep(1)

    except NoCredentialsError:
        print("ERROR: AWS credentials were not found.")
        print("Fix: run 'aws configure' in Command Prompt or Anaconda Prompt and enter your AWS access key, secret key, and region.")

    except PartialCredentialsError:
        print("ERROR: Incomplete AWS credentials found.")
        print("Fix: check your AWS access key and secret key configuration.")

    except ClientError as e:
        print("AWS Client Error:", e)

    except KeyboardInterrupt:
        print("\nScript stopped by manual intervention!")
