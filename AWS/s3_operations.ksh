aws s3 ls | awk '{print $3}' > bucket_list.out

for bucket in `cat bucket_list.out`
do

echo "Bucket $bucket contains below files: "

aws s3 ls s3://$bucket


done
