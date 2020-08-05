import boto3, uuid

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('DYNAMODB-TABLE')

# Scan table (retrieve all records)   
    response = table.scan()

    # Print response
    print(response)

    # Check if Status Code is 200    
    if response['ResponseMetadata']['HTTPStatusCode'] is 200:
        # Return Status Code and Items
        return {
            'statusCode': 200,
            'body': response['Items']
        }    





