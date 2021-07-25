import os
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import datetime
from dotenv import load_dotenv

# import GoogleSheetHelper class
from util import GoogleSheetHelper

host = "localhost"
port = 5432
username = "zelda"
password = "password"
database = "test_godo" 

db_uri = f"postgresql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(db_uri, echo=True)

load_dotenv()
cred_json = os.environ["cred_json"]

df1 = GoogleSheetHelper(cred_json, "google_postgres", "existing")
df2 = GoogleSheetHelper(cred_json, "google_postgres", "calls")
df3 = GoogleSheetHelper(cred_json, "google_postgres", "time")

# get utc now to uniquely identify backups
now = datetime.datetime.utcnow()


# existing sheet inside Users worksheet
existing_df = df1.getDataframe() #dataframe # see above
table_name = 'User_existing' + str(now)
current_utc = datetime.datetime.utcnow()
existing_df["CreatedUTC"] = current_utc
existing_df.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
)

table_df = pd.read_sql_table(
    table_name,
    con=engine
)

print(table_df.head())

# calls sheet inside Users worksheet
calls_df = df2.getDataframe() #dataframe # see above
table_name = 'User_calls' + str(now)
current_utc = datetime.datetime.utcnow()
calls_df["CreatedUTC"] = current_utc
calls_df.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
)

table_df = pd.read_sql_table(
    table_name,
    con=engine
)

print(table_df.head())

# time sheet inside Users worksheet
time_df = df3.getDataframe() #dataframe # see above
table_name = 'User_time' + str(now)
current_utc = datetime.datetime.utcnow()
time_df["CreatedUTC"] = current_utc
time_df.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
)

table_df = pd.read_sql_table(
    table_name,
    con=engine
)

print(table_df.head())

# data dict
# data = [
#         {"fullsheet" : "google_postgres", "subsheet" : "existing"},
#         {"fullsheet" : "google_postgres", "subsheet" : "calls"},
#         {"fullsheet" : "google_postgres", "subsheet" : "time"},
# ]
# for d in data:
#   gsh = GoogleSheetHelper(cred_json, d["fullsheet"], d["subsheet"])
#   
#   # get dataframe
#   gsh.getDataFrame()
#   table_name = 'backupdb_table'
#   users_df.to_sql(
#       table_name,
#       engine,
#       if_exists='replace',
#       index=False,
#       chunksize=500,
#)