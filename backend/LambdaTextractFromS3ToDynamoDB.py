import boto3

s3_client = boto3.client('s3')
textract_client = boto3.client('textract')
dynamodb_client = boto3.resource('dynamodb')

def get_s3_bucket_object(event):
    for record in event['Records']:
        return record['s3']['bucket']['name'], record['s3']['object']['key']


def download_s3_object(bucket, object):
    file_path = '/tmp/' + object
    s3_client.download_file(bucket, object, file_path)

    return file_path

def extract_text(file_path):
    with open(file_path, 'rb') as document:
        imageBytes = bytearray(document.read())

    response = textract_client.detect_document_text(Document={'Bytes': imageBytes})

    form_information = {}

    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            text = item["Text"]
            
            if text in ['Name', 'Phone', 'Account', 'Amount', 'Reason']:
                key = text
            else: 
                form_information[key] = text
    return form_information

def add_to_dynamodb(form_information):
    table = dynamodb_client.Table('DYNAMODB-TABLE')
    response = table.put_item(
        Item = form_information
    )

    print(response)

def main(event, context):
    bucket, object = get_s3_bucket_object(event)
    file_path = download_s3_object(bucket, object)

    form_information = extract_text(file_path)

    add_to_dynamodb(form_information)