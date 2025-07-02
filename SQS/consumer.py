
import boto3
from botocore.exceptions import ClientError


queue = boto3.client('sqs', region_name='us-east-1')
queue_url = 'https://sqs.us-east-1.amazonaws.com/985967191990/event_driver'

response = queue.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=10,  # Puedes ajustar este valor según tus necesidades
    WaitTimeSeconds=20  # Long Polling para esperar mensajes
)

if 'Messages' in response:
    for message in response['Messages']:
        print(f"Received message: {message['Body']}")
        
        # Procesar el mensaje aquí
        # ...

        # Eliminar el mensaje de la cola después de procesarlo
        receipt_handle = message['ReceiptHandle']
        queue.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print("Message deleted successfully.")