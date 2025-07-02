#!/bin/bash

#!/bin/bash
set -e
read -p "Enter your AWS bucket name: " BUCKET_NAME



if [ -z "$BUCKET_NAME" ]; then
    echo "No bucket name provided. Usage: $0 bucket-name"
    exit 1
fi

aws s3api list-objects --bucket "$BUCKET_NAME" --query 'Contents[].{Key: Key, Size: Size}'
