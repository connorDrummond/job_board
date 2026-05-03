select 
gen_random_uuid() as company_id,
company,
company_url,
max(company_num_employees) as company_num_employees
 from {{ source('bronze', 'jobs') }}
 where company is not null
 group by 2,3