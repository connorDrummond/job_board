select 
gen_random_uuid() as company_id,
company,
location,
company_url,
max(company_num_employees) as company_num_employees
 from postgres.bronze.jobs
 group by 1,2,3,4