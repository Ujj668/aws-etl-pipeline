Project Overview:

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using AWS services.
Raw JSON data is processed using a serverless function, cataloged, and then queried using SQL.

Tech Stack:
AWS Lambda,
Amazon S3,
AWS Glue,
Amazon Athena,
Python (Pandas)

Workflow:
a) Upload Data
b) JSON file is uploaded to S3 bucket
c) Transform Data
d) Lambda function is triggered
e) JSON is converted into a Pandas DataFrame
f) Basic transformations are applied
g) Output is stored back in S3
h) Create Table
i) Glue Crawler scans the processed data
j) Table is created in Glue Data Catalog
k) Query Data
l) Athena is used to run SQL queries on the data


Architecture
JSON File → S3 → Lambda → Transformed Data (S3) → Glue Crawler → Athena

Project Structure :
aws-etl-project/
│
├── lambda_function.py
├── sample_data.json
├── README.md

Lambda Function (Overview):
Reads JSON data from S3
Converts data into DataFrame using Pandas
Performs basic transformation
Writes processed data back to S3

IAM Roles & Permissions:
Lambda Role:
S3 read/write access
CloudWatch logs access
Glue Role:
S3 read access


Challenges Faced:

a) Handling JSON structure issues
b) Setting up S3 trigger for Lambda
c) Resolving Glue crawler table creation issues
d) Managing IAM permissions

Key Learnings:

a) Built an end-to-end ETL pipeline on AWS
b) Learned event-driven architecture
c) Gained hands-on experience with Lambda, Glue, and Athena
d) Improved data transformation using Python

Future Improvements:

a) Convert data into Parquet format for better performance
b) Add error handling and logging
c) Automate pipeline using scheduler (EventBridge)


Conclusion

This project demonstrates how AWS services can be used to build a scalable and efficient ETL pipeline without managing infrastructure
