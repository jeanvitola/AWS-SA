
import boto3
from botocore.exceptions import ClientError



queue = boto3.client('sqs', region_name='us-east-1')


queue_url = 'https://sqs.us-east-1.amazonaws.com/985967191990/event_driver'
 
for i in range(20) :
    response = queue.send_message(
        QueueUrl=queue_url,
        MessageBody=f'This is message {i+1}',
        DelaySeconds=10
    )
    print(f"Message {i+1} sent successfully.")

