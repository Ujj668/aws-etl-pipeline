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
Upload Data
JSON file is uploaded to S3 bucket
Transform Data
Lambda function is triggered
JSON is converted into a Pandas DataFrame
Basic transformations are applied
Output is stored back in S3
Create Table
Glue Crawler scans the processed data
Table is created in Glue Data Catalog
Query Data
Athena is used to run SQL queries on the data


Architecture
JSON File → S3 → Lambda → Transformed Data (S3) → Glue Crawler → Athena

Project Structure :
aws-etl-project/
│
├── lambda_function.py
├── sample_data.json
├── README.md

Sample Input Data (JSON)

{
  "batch_id": "BATCH_001",
  "source": "ecommerce_app",
  "upload_date": "2026-04-05",
  "region": "IN",
  "orders": [
    {
      "transaction_id": "T001",
      "date": "2026-04-01",
      "customer_id": "C101",
      "product": "Mobile",
      "amount": 15000,
      "payment_method": "UPI"
    },
    {
      "transaction_id": "T002",
      "date": "2026-04-02",
      "customer_id": "C102",
      "product": "Headphones",
      "amount": 2500,
      "payment_method": "Card"
    },
    {
      "transaction_id": "T003",
      "date": "2026-04-03",
      "customer_id": "C103",
      "product": "Keyboard",
      "amount": 1200,
      "payment_method": "Cash"
    }
  ]
}


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

Handling JSON structure issues
Setting up S3 trigger for Lambda
Resolving Glue crawler table creation issues
Managing IAM permissions

Key Learnings:

Built an end-to-end ETL pipeline on AWS
Learned event-driven architecture
Gained hands-on experience with Lambda, Glue, and Athena
Improved data transformation using Python

Future Improvements:

Convert data into Parquet format for better performance
Add error handling and logging
Automate pipeline using scheduler (EventBridge)


Conclusion

This project demonstrates how AWS services can be used to build a scalable and efficient ETL pipeline without managing infrastructure
