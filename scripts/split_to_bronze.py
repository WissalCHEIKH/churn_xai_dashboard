import pandas as pd

# Load the full dataset
df = pd.read_csv('data/raw/telco_ibm.csv')

# --- CRM / socio-demographic ---
crm_colls = ["customerID", "gender", "SeniorCitizen", "Partner", "Dependents"]
crm_table = df[crm_colls]
crm_table.to_csv("data/bronze/raw_crm.csv", index=False)

# --- Services / usage ---
service_colls = ["customerID", "PhoneService", "MultipleLines", "InternetService",
                  "OnlineSecurity", "DeviceProtection", "TechSupport",
                  "StreamingTV", "StreamingMovies", "OnlineBackup"]
service_table = df[service_colls]
service_table.to_csv("data/bronze/raw_service.csv", index=False)

# --- Billing / account (includes tenure = contractual commitment) ---
billing_colls = ["customerID", "Contract", "PaperlessBilling", "PaymentMethod",
                  "MonthlyCharges", "TotalCharges", "tenure"]
billing_table = df[billing_colls]
billing_table.to_csv("data/bronze/raw_billing.csv", index=False)

# --- Label, kept separate (not a source system, the prediction target) ---
label_colls = ["customerID", "Churn"]
label_table = df[label_colls]
label_table.to_csv("data/bronze/churn_label.csv", index=False)