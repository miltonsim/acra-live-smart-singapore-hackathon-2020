import json
import boto3
import uuid 


def lambda_handler(event, context):
    if event['Records'][0]['eventName'] == "INSERT":
        
        try:
        
            a2i = boto3.client('sagemaker-a2i-runtime', region_name='us-east-1')
            
            sm_rt = boto3.Session().client('runtime.sagemaker', region_name='us-east-1')
            
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('DYNAMODB-TABLE')
            
            SCORE_THRESHOLD = .52
            
            human_loops_started = []
            
            ep_name = 'SAGEMAKER-ENDPOINT'
            flowDefinitionArn  = 'FLOW-DEFINITION-ARN'
            
            stream = event["Records"][0]["dynamodb"]["NewImage"]
            data = f"{stream['Name']['S']},{stream['Phone']['S']},{stream['Account']['S']},{stream['Amount']['S']},{stream['Reason']['S']}"
    
            response = sm_rt.invoke_endpoint(EndpointName=ep_name, ContentType='text/csv', Accept='text/csv', Body=data)
            
            response = response['Body'].read().decode("utf-8")
            response = response.split(',')
            
            outcome = response[0]
            score = float(response[1])
            
            if(outcome == "n"):
                score -= 1
                score = abs(score)
            
            print(f"\nOutcome: {outcome}, Probability Score: {score}\n")
            
            result = ""
            if (outcome=="y" and score < SCORE_THRESHOLD or outcome=="n" and score < SCORE_THRESHOLD):
                
                result = "Pending Review"
                
                humanLoopName = str(uuid.uuid4())
                
                data = data.split(',')
                
                inputContent = {
                    "name": data[0],
                    "phone_number": data[1],
                    "account_number": data[2],
                    "amount": data[3],
                    "reason": data[4],
                    "outcome": outcome,
                    "score": score,
                }
            
                start_loop_response = a2i.start_human_loop(
                    HumanLoopName=humanLoopName,
                    FlowDefinitionArn=flowDefinitionArn,
                    HumanLoopInput={
                        "InputContent": json.dumps(inputContent)
                    }
                )
                human_loops_started.append(humanLoopName)
                
                print(f'Starting human loop: {humanLoopName}  \n')
            
            else:
                if(outcome == "y"):
                    result = "Approved"
                else:
                    result = "Rejected"
            
            response = table.update_item(
                Key={
                    'Name': stream['Name']['S'],
                },
                UpdateExpression="set Stage = :s",
                ExpressionAttributeValues={
                    ':s': result
                }
            )
        except:
            pass
