from jobspy import scrape_jobs
import pandas as pd
from sqlalchemy import create_engine
jobs_list = [
    "Software Engineer",
    "Data Engineer",
    "Data Scientist",
    "Data Analyst",
    "Analytics Engineer"
]

data = pd.DataFrame()

for job in jobs_list:
    jobs = scrape_jobs(
        site_name="indeed",
        search_term=job,
        google_search_term="Data engineer jobs near Kansas City, MO since yesterday",
        verbose=1,
        results_wanted=20000,
        is_remote=True,
        country_indeed='USA',
    )

    jobs_df = pd.DataFrame(jobs)
    data = pd.concat([data, jobs_df], axis=0, ignore_index=True)

conn_string = 'postgresql://postgres:14Cd1442$@database-2.cf28q0kociwu.us-east-2.rds.amazonaws.com:5432/postgres'
db = create_engine(conn_string)

data.to_sql('jobs', con=db, if_exists='append', index=False, schema = 'silver')