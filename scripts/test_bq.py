from google.oauth2 import service_account
from google.cloud import bigquery

key = r"C:\Users\lenovo\Desktop\churn_xai_dashboard\dbt_project\keys\bq-key.json"
creds = service_account.Credentials.from_service_account_file(key)
client = bigquery.Client(credentials=creds, project="thinking-field-468009-s0")
print(list(client.query("select 1 as id").result()))