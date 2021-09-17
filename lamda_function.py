import json
import boto3 #Library with aws for python access to aws
#Machine learning tool using aws 


def lambda_handler(event, context):
    rekognition = boto3.client("rekognition") #Getting image rekognition service
    s3 = boto3.client("s3") #Connected rekognition and s3 to client 
    fileObj = s3.get_object(Bucket= "imgrecognitiontahmidurbucket", Key ="Carpathian-Lynx-1.png") #Saving file object
    file_content = fileObj["Body"].read()
    response = rekognition.detect_labels(Image = {"S3Object": {"Bucket": "imgrecognitiontahmidurbucket", "Name": "Carpathian-Lynx-1.png"}}) #AWS function to recognize feature of image
    # TODO implement
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

#Deploy, then test
#program recognizes content of image and dimmensions 
