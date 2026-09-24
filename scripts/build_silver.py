import pandas as pd

crm = pd.read_csv("data/bronze/raw_crm.csv")
service = pd.read_csv("data/bronze/raw_service.csv")
billing = pd.read_csv("data/bronze/raw_billing.csv")

# Fix the known data quality issue: TotalCharges has blank strings for tenure=0 customers
billing["TotalCharges"] = billing["TotalCharges"].replace(" ", "0")
billing["TotalCharges"] = billing["TotalCharges"].astype(float)

# Join all 3 on customerID
silver = crm.merge(service, on="customerID").merge(billing, on="customerID")

silver.to_csv("data/silver/customers_silver.csv", index=False)
print("Silver table shape:", silver.shape)