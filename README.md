
<a  href="https://github.com/Xenonwizard/ACRA-Live-Smart"><img  src="https://drive.google.com/uc?export=view&id=1JmPW6yu3J_pRZGc7HGvjRiU_wvSglJcx"  height="400"  width="520"/></a>

# Live Smart Hackathon (Ree-Cloud)

>**Short Introduction**

We are a team from Nanyang Polytechnic consisting of Ryan Ho, Eugene Foo, Milton Sim and Elijah Chia. We created an AI solution using AWS “Sagemaker”, “Textract” and “A2I” to automate waiver form processing for ACRA.

**Our Solution**

> Our solution uses Textract to extract text field data from uploaded documents. Then gets “Sagemaker” to pull these entries and match the data against a “Kaggle” dataset of 40000 bank customer entries. Using an XGBoost ML Algorithm, each document would then produce a confidence score at a 92% objectivity rating. The solution also utilizes AWS “A2i” to produce a human review workflow for a private team of workers to validate the approval of forms which failed the metric checks of the AI. 

**Amazon Services Used**

- SageMaker

- Augmented Artificial Intelligence (A2I)

- Lambda

- Simple Storage Service (S3 )

- API Gateway

- DynamoDB

- Presigned URLs

  

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Dependency Status](http://img.shields.io/gemnasium/badges/badgerbadgerbadger.svg?style=flat-square)](https://gemnasium.com/badges/badgerbadgerbadger) [![Coverage Status](http://img.shields.io/coveralls/badges/badgerbadgerbadger.svg?style=flat-square)](https://coveralls.io/r/badges/badgerbadgerbadger) [![Code Climate](http://img.shields.io/codeclimate/github/badges/badgerbadgerbadger.svg?style=flat-square)](https://codeclimate.com/github/badges/badgerbadgerbadger) [![Gem Version](http://img.shields.io/gem/v/badgerbadgerbadger.svg?style=flat-square)](https://rubygems.org/gems/badgerbadgerbadger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) [![Badges](http://img.shields.io/:badges-9/9-ff6799.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger)

---

## OVERVIEW OF OUR ARCHITECTURE

<br/>

  
  

<img  src="https://drive.google.com/uc?export=view&id=15fIEhtdbk6H7LzBVWdjs-I45NhwwI1ZU"/>  <br/>

  
  
  
  

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

Case status can be viewed (on-going and closed)

  

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

  

https://github.com/Xenonwizard/ACRA-Live-Smart/tree/master/Lambda

https://github.com/Xenonwizard/ACRA-Live-Smart/tree/master/S3-Website

https://github.com/Xenonwizard/ACRA-Live-Smart/blob/master/a2i-worker-task-template.html

  

Training/Test Data Used:

  

https://github.com/Xenonwizard/ACRA-Live-Smart/blob/master/sagemaker-training-data.csv

https://github.com/Xenonwizard/ACRA-Live-Smart/blob/master/Team%20Photo.jpeg

  

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

  

For a reference on the human loop and A2i that needs to be made you can refer to <a  href="https://aws.amazon.com/blogs/machine-learning/object-detection-and-model-retraining-with-amazon-sagemaker-and-amazon-augmented-ai/">here</a>. However do note that you will need to make the appropriate changes as this is an <b>object detection</b> example but what we are doing is <b>document processing</b>.

  
  

---

  

## Features

## Usage (Optional)

## Documentation (Optional)

## Tests (Optional)

  

- Going into more detail on code and technologies used

- I utilized this nifty <a  href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"  target="_blank">Markdown Cheatsheet</a> for this sample `README`.

  

---

  

## Contributing

  

> To get started...

  

### Step 1

  

-  **Option 1**

- 🍴 Fork this repo!

  

-  **Option 2**

- 👯 Clone this repo to your local machine using `https://github.com/joanaz/HireDot2.git`

  

### Step 2

  

-  **HACK AWAY!** 🔨🔨🔨

  

### Step 3

  

- 🔃 Create a new pull request using <a  href="https://github.com/joanaz/HireDot2/compare/"  target="_blank">`https://github.com/joanaz/HireDot2/compare/`</a>.

  

---

  

## Team

  

> Or Contributors/People

  

| <a  href="http://fvcproductions.com"  target="_blank">**FVCproductions**</a> | <a  href="http://fvcproductions.com"  target="_blank">**FVCproductions**</a> | <a  href="http://fvcproductions.com"  target="_blank">**FVCproductions**</a> |

| :---: |:---:| :---:|

| [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) |

| <a  href="http://github.com/fvcproductions"  target="_blank">`github.com/fvcproductions`</a> | <a  href="http://github.com/fvcproductions"  target="_blank">`github.com/fvcproductions`</a> | <a  href="http://github.com/fvcproductions"  target="_blank">`github.com/fvcproductions`</a> |

  

- You can just grab their GitHub profile image URL

- You should probably resize their picture using `?s=200` at the end of the image URL.

  

---

  

## FAQ

  

-  **What is the estimated cost of each processed document?**

- Each document as of now would cost roughly less than $1.00 for processing. However, prices are subjected to "Economies of Scale" as you use it more.

  
  

---

  

## Support

  

Reach out to me at one of the following places!

  

- Website at <a  href="http://fvcproductions.com"  target="_blank">`fvcproductions.com`</a>

- Twitter at <a  href="http://twitter.com/fvcproductions"  target="_blank">`@fvcproductions`</a>

- Insert more social links here.

  
  
  

## License

  

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

  

-  **[MIT license](http://opensource.org/licenses/mit-license.php)**

- Copyright 2015 © <a  href="http://fvcproductions.com"  target="_blank">FVCproductions</a>.