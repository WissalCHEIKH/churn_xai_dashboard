select
    customerID as customer_id,
    case when cast(Churn as string) in ('true', 'Yes') then 1 else 0 end as churn_j30
from {{ source('raw', 'churn_label') }}