from os import environ
from sqlalchemy import create_engine
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy.types import Integer, Text, String, DateTime

host = "localhost"
port = 5432
username = "zelda"
password = "password"
database = "some_db" 

db_uri = f"postgresql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(db_uri, echo=True)

jobs_df = pd.read_csv('data/nyc-jobs.csv')
table_name = 'nyc_jobs'

jobs_df.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    dtype={
        "job_id": Integer,
        "agency": Text,
        "business_title": Text,
        "job_category":  Text,
        "salary_range_from": Integer,
        "salary_range_to": Integer,
        "salary_frequency": String(50),
        "work_location": Text,
        "division/work_unit": Text,
        "job_description": Text,
        "posting_date": DateTime,
        "posting_updated": DateTime
    }
)

table_df = pd.read_sql_table(
    table_name,
    con=engine
)