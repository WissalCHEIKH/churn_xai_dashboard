select
    customerID as customer_id,
    PhoneService as has_phone_service,
    MultipleLines as multiple_lines,
    InternetService as internet_service,
    OnlineSecurity as online_security,
    OnlineBackup as online_backup,
    DeviceProtection as device_protection,
    TechSupport as tech_support,
    StreamingTV as streaming_tv,
    StreamingMovies as streaming_movies
from {{ source('raw', 'raw_service') }}