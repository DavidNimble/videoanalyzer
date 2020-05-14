# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='robinvideolyzervideos')
bucket = s3.create_bucket(Bucket='robinvideolyzervideos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='robinvideolyzervideos101')
from pathlib import Path 
get_ipython().run_line_magic('ls', '/home/DaveisChad/Downloads/lovelyrunning.mp4')
pathname = '/home/DaveisChad/Downloads/lovelyrunning.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
rekognition_client = session.client(region_name:'us-east-1', 'rekognition')
rekognition_client = session.client('rekognition', region_name = 'us-east-1' )
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result 
result['Jobstatus']
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
len(result['Labels'])
