select
    customerID as customer_id,
    gender,
    SeniorCitizen as senior_citizen,
    Partner as has_partner,
    Dependents as has_dependents
from {{ source('raw', 'raw_crm') }}