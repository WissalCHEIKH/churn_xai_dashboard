select
    customerID as customer_id,
    Contract as contract,
    PaperlessBilling as is_paperless_billing,
    PaymentMethod as payment_method,
    MonthlyCharges as monthly_charges,
    coalesce(safe_cast(nullif(trim(TotalCharges), '') as float64), 0) as total_charges,
    tenure
from {{ source('raw', 'raw_billing') }}