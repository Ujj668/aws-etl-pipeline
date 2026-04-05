import json
import boto3
import pandas as pd
import io

def flatten(data):
    
    if isinstance(data, dict):
        data = [data]

    orders_data = []

    for i in data:
        orders = i.get('orders', [])
        for j in orders:
            row_orders = {
                "batch_id": i.get("batch_id"),
                "source": i.get("source"),
                "upload_date": i.get("upload_date"),
                "region": i.get("region"),
                "transaction_id": j.get("transaction_id"),
                "date": j.get("date"),
                "customer_id": j.get("customer_id"),
                "product": j.get("product"),
                "amount": j.get("amount"),
                "payment_method": j.get("payment_method")
            }
            orders_data.append(row_orders)

    return pd.DataFrame(orders_data)


def lambda_handler(event, context):
    print("Lambda triggered")

    try:
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']

        target_bucket = "orders-outgoing-1"

        s3 = boto3.client("s3")

        response = s3.get_object(Bucket=source_bucket, Key=file_name)
        content = response['Body'].read().decode('utf-8')
        data = json.loads(content)

        df = flatten(data)
        print("DataFrame created:", df.shape)

        buffer = io.BytesIO()
        df.to_parquet(buffer, index=False)

        output_key = file_name.replace(".json", ".parquet")

        s3.put_object(
            Bucket=target_bucket,
            Key=output_key,
            Body=buffer.getvalue()
        )

        print(f"Parquet file saved to {target_bucket}/{output_key}")

        return {
            'statusCode': 200,
            'body': json.dumps('Parquet file created successfully')
        }

    except Exception as e:
        print("Error:", str(e))
        raise e