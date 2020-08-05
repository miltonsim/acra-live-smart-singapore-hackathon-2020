import boto3, csv, json, time

TABLE_NAME = 'DYNAMODB-TABLE'
OUTPUT_BUCKET = 'S3-BUCKET'
TEMP_FILENAME = '/tmp/output.csv'
OUTPUT_KEY = f'output-{str(int(time.time()))}.csv'

s3_resource = boto3.resource('s3')
dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table(TABLE_NAME)

def lambda_handler(event, context):
    with open(TEMP_FILENAME, 'w') as output_file:
        writer = csv.writer(output_file)
        header = True
        first_page = True

        # Paginate results
        while True:
            # Scan DynamoDB table
            if first_page:
                response = table.scan()
                first_page = False
            else:
                response = table.scan(ExclusiveStartKey = response['LastEvaluatedKey'])

            for item in response['Items']:

                # Write header row?
                if header:
                    writer.writerow(item.keys())
                    header = False

                writer.writerow(item.values())

            # Last page?
            if 'LastEvaluatedKey' not in response:
                break
    
    upload_file_to_s3()
    return create_presigned_url()

def upload_file_to_s3():
    # Upload temp file to S3    
    s3_resource.Bucket(OUTPUT_BUCKET).upload_file(TEMP_FILENAME, OUTPUT_KEY)


def create_presigned_url():
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')

    expiration=3600

    response = s3_client.generate_presigned_url('get_object',Params={'Bucket': OUTPUT_BUCKET,'Key': OUTPUT_KEY},ExpiresIn=expiration)    

    return(response)