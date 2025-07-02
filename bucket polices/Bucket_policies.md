


# create a bucket

aws s3 mb s3://bucket-policy-example-ab-523565
# los nombres de los bucket deben ser únicos e irrepetibles, si se intenta crear por ejemplo un bucket de algún tutorial este lo catalogará como ya existente y mandará error


## put bucket

aws s3api put-bucket-policy --bucket bucket-policy-example-ab-523565 --policy file://policy.json



## Apply Policies
# la politica establecida en el archivo Json tendrá efecto inmediatamente, als politicas pueden ser de accesos, de cifrado, de cambiar el bucket a público y cientos de elementos más.