import pandas as pd

silver = pd.read_csv("data/silver/customers_silver.csv")
label = pd.read_csv("data/bronze/churn_label.csv")

gold = silver.merge(label, on="customerID")

# Encode target
gold["churn_j30"] = (gold["Churn"] == "Yes").astype(int)
gold = gold.drop(columns=["Churn"])

# One-hot encode categorical columns, keep customerID and label out of encoding
cat_cols = gold.select_dtypes(include="object").columns.tolist()
cat_cols.remove("customerID")
gold_encoded = pd.get_dummies(gold, columns=cat_cols, drop_first=True)

gold_encoded.to_csv("data/gold/customer_churn_features.csv", index=False)
print("Gold table shape:", gold_encoded.shape)
print("Churn rate:", gold_encoded["churn_j30"].mean())