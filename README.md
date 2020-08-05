
<a href="https://github.com/Xenonwizard/ACRA-Live-Smart"><img  src="./readme_resources/TeamPhoto.jpeg"  height="500"  width="520"/></a>

# Live Smart Hackathon (Ree-Cloud)

**Short Introduction**

>We are a team from Nanyang Polytechnic consisting of Ryan Ho, Eugene Foo, Milton Sim and Elijah Chia. We created an solution in AWS using  Sagemaker, Textract and A2I to automate waiver form processing for ACRA.

**Our Solution**
> Our solution involves a serverless web application that is hosted in S3 which allows ACRA staff members to view case details and upload a scannned copy of their waiver process form into S3. A Lambda function will be triggered and leverage on Textract to extract text field data into DynamoDB. This would tigger a DynamoDB update stream and call another Lambda function to make a request to the Sagemaker endpoint for automatic decision making of cases. This solution also utilizes Augmented AI to produce a human review workflow for a private team of workers to validate the approval of forms if the Machine Learning model is not confident on the outcome. 

**Amazon Services Used**

- SageMaker

- Augmented AI (A2I)

- Lambda

- API Gateway

- DynamoDB

- Simple Storage Service (S3)

---

## OVERVIEW OF OUR ARCHITECTURE

<br/>
<img  src="https://drive.google.com/uc?export=view&id=15fIEhtdbk6H7LzBVWdjs-I45NhwwI1ZU"/> 
<br/>

**Request**
<img  src="https://drive.google.com/uc?export=view&id=1OIvltuv7foSDCd6vsH6vPi9MxhBUpxuo"  height="400"/><br/>

*Hard Copy Form*

- Customer submits hard copy form to ACRA staff

- Staff scans and uploads the document to the staff website where it will be stored in AWS S3

- The uploading of the document to S3 triggers AWS Lambda and AWS Textract to extract text elements from the document and stores this information in AWS DynamoDB

Online Form

- Customer submits online form on the customer website

- Form details are stored in Amazon DynamoDB

*Helpdesk and Chatbot*

- Customer can chat with chatbot which utilises AWS Lex

- Customer can make enquiries to the helpdesk through AWS Connect

**Review**

<img  src="https://drive.google.com/uc?export=view&id=1AMI2QFUC7IBy7R6ePVoxqSQNP4uZd1XU"  /><br/>

*Decision Making Engine*

- Once form details are added to AWS DynamoDB, AWS Lambda is automatically triggered where it will make use of Amazon SageMaker to determine if the case should be approved.

*Dashboard*

- The staff views the staff website which is hosted on AWS S3

- The website makes use of Amazon API Gateway and AWS Lambda to retrieve the case records from AWS DynamoDB

Case status can be viewed (Approved, Rejected, Pending Review)

**Refund/Reply**

<img  src="https://drive.google.com/uc?export=view&id=1Mbmarr9PPPDUM8m2XT_C052eHZCLTkNm"/><br/>

*Customer Notification*

When a case if approved or rejected, customers will be notified via email using AWS SES

*Refund*

When a case is approved, AWS Lambda is triggered and submits a refund to the customer through the payment gateway

**Record**

<img  src="https://drive.google.com/uc?export=view&id=1fF7WSg6nUlfSUFfK6oU-owkGxiANjwgz"/><br/>

*Excel Records*

Staff requests to view the excel spreadsheet.

This triggers Amazon API Gateway and AWS Lambda to retrieve records from AWS DynamoDB and export it as an excel spreadsheet

Spreadsheet is stored in AWS S3 where it can be downloaded

---

## SETUP/USAGE/HOW TO

These are the code resources that we created:

[Lambda](backend/)

[Website Dashboard](frontend/dashboard.html)

[Website File Upload](frontend/upload_file.html)

[A2i Worker Task Template](frontend/a2i-worker-task-template.html)

<!-- https://github.com/Xenonwizard/ACRA-Live-Smart/tree/master/Lambda

https://github.com/Xenonwizard/ACRA-Live-Smart/tree/master/S3-Website -->

<!-- https://github.com/Xenonwizard/ACRA-Live-Smart/blob/master/a2i-worker-task-template.html -->

Training/Test Data Used:

[Training Data](project_resources/sagemaker-training-data.csv)
<!-- https://github.com/Xenonwizard/ACRA-Live-Smart/blob/master/sagemaker-training-data.csv -->

<!-- https://github.com/Xenonwizard/ACRA-Live-Smart/blob/master/Team%20Photo.jpeg -->

---

## Prerequisite

- All resources can be accessed in AWS Console

- For AI related training, it would be highly recommended for you to use AWS Sagemaker Studio. This is because it includes all the required imports

- Get familiar with Python programming in Jupyter Notebook and Lambda.

- Follow the diagrams provided

- But if all else fails you can contact us

### Setup

We have already included everything for you but if there are issues:

Please ensure that you have the following imports:

```

import boto3, csv, json, time, uuid

```

Also ensure that you have called your resource every time you are coding.

For example 1:

```

s3_client = boto3.client('s3')

textract_client = boto3.client('textract')

dynamodb_client = boto3.resource('dynamodb')

```

For example 2:

```

dynamodb = boto3.resource(

'dynamodb',

aws_access_key_id="**********",

aws_secret_access_key="*************",

region_name='ap-southeast-1'

```

For Autopilot Setup refer to the tutorial<a  href="https://aws.amazon.com/getting-started/hands-on/create-machine-learning-model-automatically-sagemaker-autopilot/"  target="_blank"> here </a></p>

For the A2I worker template, you can refer to the "Example Example of an automated classification template." example on this <a  href="https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-custom-templates.html">webpage</a>

For a reference on the human loop and A2i that needs to be made, you can refer to <a  href="https://aws.amazon.com/blogs/machine-learning/object-detection-and-model-retraining-with-amazon-sagemaker-and-amazon-augmented-ai/">here</a>. However do note that you will need to make the appropriate changes as this is an <b>object detection</b> example but what we are doing is <b>document processing</b>.