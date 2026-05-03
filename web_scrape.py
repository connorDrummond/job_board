import jobspy


import pandas as pd
from sqlalchemy import create_engine
import os
jobs_list = [
    "Software Engineer",
    "Data Engineer",
    "Data Scientist",
    "Data Analyst",
    "Analytics Engineer"
]

data = pd.DataFrame()

for job in jobs_list:
    jobs = jobspy.scrape_jobs(
        site_name="indeed",
        search_term=job,
        google_search_term="Data engineer jobs near Kansas City, MO since yesterday",
        verbose=1,
        results_wanted=5000,
        is_remote=True,
        country_indeed='USA',
    )

    jobs_df = pd.DataFrame(jobs)
    data = pd.concat([data, jobs_df], axis=0, ignore_index=True)


conn_string = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:5432/{os.environ['DB_NAME']}"
db = create_engine(conn_string)

data.to_sql('jobs', con=db, if_exists='append', index=False, schema = 'bronze')