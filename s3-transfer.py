import boto3

s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('D:\Dokumenty\IT\AWS\zyczenie.jpeg', 'rb')
s3.Bucket('my-sample-bucket-inga').put_object(Key='zyczenie.jpeg', Body=data)
print("Done")

# Upload a file ('name of the file', 'bucket name', 'name of saved file')
#s3.upload_file('', '', '')