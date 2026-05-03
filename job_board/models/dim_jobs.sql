select 
gen_random_uuid() as job_id,
j.title,
j.job_url,
c.company_id,
l.location_id,
j.min_amount,
j.max_amount,
j.date_posted
from {{ source('bronze', 'jobs') }} j 
left join {{ ref('dim_locations') }} l 
on l.location = j.location 
left join {{ ref('dim_companies') }} c 
on c.company = j.company
where j.title is not null and c.company is not null 