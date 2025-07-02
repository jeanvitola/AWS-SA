


import boto3
from botocore.exceptions import ClientError 



sqs = boto3.client('sqs')  
response = sqs.list_queues()    
sqs_response_list = response.get('QueueUrls', [])   
print(f"List of SQS Queues:{sqs_response_list}")