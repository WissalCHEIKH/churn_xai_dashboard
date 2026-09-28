select
    c.customer_id,
    c.gender,
    c.senior_citizen,
    c.has_partner,
    c.has_dependents,
    s.has_phone_service,
    s.multiple_lines,
    s.internet_service,
    s.online_security,
    s.online_backup,
    s.device_protection,
    s.tech_support,
    s.streaming_tv,
    s.streaming_movies,
    b.contract,
    b.is_paperless_billing,
    b.payment_method,
    b.monthly_charges,
    b.total_charges,
    b.tenure,
    l.churn_j30
from {{ ref('stg_crm') }} c
join {{ ref('stg_service') }} s on c.customer_id = s.customer_id
join {{ ref('stg_billing') }} b on c.customer_id = b.customer_id
join {{ ref('stg_churn_label') }} l on c.customer_id = l.customer_id