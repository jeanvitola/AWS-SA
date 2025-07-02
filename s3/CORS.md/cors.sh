# create a bucket

 aws s3 mb s3://corn-origin-test-lab

# change block public access


aws s3api put-public-access-block \
    --bucket corn-origin-test-lab\
    --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"

# create a bucket policy
aws s3api put-bucket-policy --bucket corn-origin-test-lab --policy file://policy.json

# turn on statics website hosting
aws s3 website s3://corn-origin-test-lab/ --index-document index.html

# copy the index.html file to the bucket
aws s3 cp index.html s3://corn-origin-test-lab/



# view the website and see if the index.html is there
http://corn-origin-test-lab.s3-website-us-east-1.amazonaws.com/

# upload our index.html file and include a resource that would be cross-origin
aws s3 cp index.html s3://corn-origin-test-lab/index.html

# apply a CORS policy
aws s3api put-bucket-cors \
    --bucket corn-origin-test-lab \
    --cors-configuration file://cors.json
    # view the CORS policy
