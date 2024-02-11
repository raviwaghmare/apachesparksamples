import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('344433430712-test-bucket-rkw')
for obj in bucket.objects.all():
    print(obj.key)
