select 
Distinct
gen_random_uuid() as location_id,
location,
min(date_posted) as date_created
from {{ source('bronze', 'jobs') }}
group by 1,2