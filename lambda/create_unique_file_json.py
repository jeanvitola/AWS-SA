import boto3
import json
import os
from faker import Faker

def create_one_large_file():
    """Create one large JSON file with ~3000 records."""
    faker = Faker()
    os.makedirs('output', exist_ok=True)
    data = []

    for i in range(1, 3001):
        record = {
            "id": i,
            "name": faker.name(),
            "email": faker.email(),
            "company": faker.company(),
            "active": faker.boolean()
        }
        data.append(record)

    # Guardar el único archivo JSON
    with open("output/batch_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ File 'batch_data.json' created with 3000 records.")

def s3_upload_files():
    """Upload files from the output directory to S3."""
    bucket_name = 'test-sqs-lambda-lab-2'
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)

    for root, dirs, files in os.walk('output'):
        for file in files:
            local_path = os.path.join(root, file)
            s3_key = os.path.relpath(local_path, 'output').replace('\\', '/')

            print(f"Uploading {local_path} as {s3_key}...")
            bucket.upload_file(local_path, s3_key)

    print("✅ All files have been uploaded successfully.")

if __name__ == "__main__":
    create_one_large_file()
    s3_upload_files()
