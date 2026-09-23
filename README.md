# Churn Prediction Pipeline with XAI

Telco customer churn prediction with explainable AI (SHAP/LIME), 
built following a medallion architecture (Bronze/Silver/Gold).

## Structure
- data/ - raw, bronze, silver, gold layers (data itself is gitignored)
- scripts/ - data extraction and transformation scripts
- ml/ - model training and explainability code
- dashboard/ - Power BI files/exports
- docs/ - architecture diagrams
- dbt_project/ - dbt models (Silver/Gold transformations)