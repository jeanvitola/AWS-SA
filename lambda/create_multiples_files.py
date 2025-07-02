import boto3
from botocore.exceptions import ClientError
import json 
import os 

# Create a directory if no exists



def create_multiples_files() :
    """Create multiple JSON files with sample data."""
    pass
    os.makedirs('output', exist_ok=True)

    for i in range (1,20) :
        data = {
            "id": i,
            "name": f"Item {i}",
            "description": f"This is item number {i}."
        }
        print(f"Creating file {i} with data: {data}")

    # guardar el archivo
        with open (f"output/item_{i}.json", 'w') as f:
            json.dump(data, f)
    print("✅ All files have been created successfully.")


def s3_upload_files() :
    """Upload files from the output directory to S3."""
    bucket_name = 'test-end-lambda-jeanvitola'
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
    create_multiples_files()
    s3_upload_files()