# Live Smart Hackathon (Ree-Cloud)

<img  src="./readme_resources/TeamPhoto.jpeg"  height="400" />

Members | Position
------ | -----
Milton Sim | Top
Eugene Foo | Center
Ryan Lucas Ho | Center
Elijah Chia | Bottom

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
<img  src="./readme_resources/ACRA_Architecture.png" height="400"/> 
<br/>

**Request**
<img  src="./readme_resources/Request.png"  height="400"/><br/>

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

<img  src="./readme_resources/Review.png" height="400"/><br/>

*Decision Making Engine*

- Once form details are added to AWS DynamoDB, AWS Lambda is automatically triggered where it will make use of Amazon SageMaker to determine if the case should be approved.

*Dashboard*

- The staff views the staff website which is hosted on AWS S3

- The website makes use of Amazon API Gateway and AWS Lambda to retrieve the case records from AWS DynamoDB

Case status can be viewed (Approved, Rejected, Pending Review)

**Refund/Reply**

<img  src="./readme_resources/Refund-Reply.png" height="400"/><br/>

*Customer Notification*

When a case if approved or rejected, customers will be notified via email using AWS SES

*Refund*

When a case is approved, AWS Lambda is triggered and submits a refund to the customer through the payment gateway

**Record**

<img  src="./readme_resources/Record.png" height="400"/><br/>

*Excel Records*

Staff requests to view the excel spreadsheet.

This triggers Amazon API Gateway and AWS Lambda to retrieve records from AWS DynamoDB and export it as an excel spreadsheet

Spreadsheet is stored in AWS S3 where it can be downloaded

---

## Prerequisite

- All resources can be accessed in AWS Console

- For AI related training, it would be highly recommended for you to use AWS Sagemaker Studio. This is because it includes all the required imports

- Get familiar with Python programming in Jupyter Notebook and Lambda.

- Follow the diagrams provided

- But if all else fails you can contact us

### Setup

1. Clone this repository
2. Train a Sagemaker model using [Autopilot](https://aws.amazon.com/getting-started/hands-on/create-machine-learning-model-automatically-sagemaker-autopilot/) and deploy it
3. Create an [A2i](https://aws.amazon.com/blogs/machine-learning/object-detection-and-model-retraining-with-amazon-sagemaker-and-amazon-augmented-ai) human loop
5. Create a Lambda function for each [backend file](backend/)
    - Remember to include the DynamoDB table, A2i workflow ARN, S3 bucket location and Sagemaker endpoint in the python files
6. Deploy the Website Dashboard and File Upload pages into AWS S3

## Resources

[Lambda](backend/)

[Website Dashboard](frontend/dashboard.html)

[Website File Upload](frontend/upload_file.html)

[A2i Worker Task Template](frontend/a2i-worker-task-template.html)

[Training Data](project_resources/sagemaker-training-data.csv)
