import requests
import pandas as pd
import boto3
from io import StringIO

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert to CSV
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# Upload to S3
s3 = boto3.client(
    's3',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

s3.put_object(
    Bucket='your-bucket-name',
    Key='users.csv',
    Body=csv_buffer.getvalue()
)

print("File uploaded successfully")
