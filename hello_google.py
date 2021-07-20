import os
import gspread
import pandas as pd
from gspread_pandas import Spread, Client
from oauth2client.service_account import ServiceAccountCredentials
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import datetime

"""
# REMINDER: must share email located in key by pressing "share" button in google sheets to share with the credential email or it wont work!
"""

# input
#cred_json = os.environ['json_path']
cred_json = "/home/batman/Desktop/google_postgres/key/master_key.json"
# TODO: accept arguments to initialize class with kwawgs
class GoogleSheetHelper:
    def __init__(self, key_path, spreadsheetName, sheetName):
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.key_path = key_path
        self.spreadsheetName = spreadsheetName
        self.sheetName = sheetName

    def sheetToDataframe(self):
        pass

    def getDataframe(self):
        spreadsheet = client.open(self.spreadsheetName)
        sheet = spreadsheet.worksheet(self.sheetName)
        rows = sheet.get_all_records()
        return pd.DataFrame(rows)

""" Function for gathering profile information from the Client"""
# check data in spreadsheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(cred_json, scope)
client = gspread.authorize(creds)

# get worksheet name and specific sheet inside the worksheets name
spreadsheetName = "google_postgres"
sheetName = "time"

# open appropriate spreadsheet
spreadsheet = client.open(spreadsheetName)
sheet = spreadsheet.worksheet(sheetName)
rows = sheet.get_all_records()
print(type(rows)) # list of dictionaries (ideal!)

# convert dict rows to pandas dataframe
dataframe = pd.DataFrame(rows)
print(dataframe)

df1 = GoogleSheetHelper(cred_json, "google_postgres", "existing")
df2 = GoogleSheetHelper(cred_json, "google_postgres", "calls")
df3 = GoogleSheetHelper(cred_json, "google_postgres", "time")

print(df1.getDataframe().head())
print("*" * 50)
print(df2.getDataframe().head())
print("*" * 50)
print(df3.getDataframe().head())

###############################################################################
# Now that we have data from googlesheetsAPI, insert to goanddo PostgresSQL
###############################################################################
# host = "localhost"
# port = 5432
# username = "zelda"
# password = "password"
# database = "godo0" 

# db_uri = f"postgresql://{username}:{password}@{host}:{port}/{database}"
# engine = create_engine(db_uri, echo=True)

# jobs_df = dataframe # see above
# table_name = 'google_sheet_data'
# current_utc = datetime.datetime.utcnow()
# jobs_df["CreatedUTC"] = current_utc
# jobs_df.to_sql(
#     table_name,
#     engine,
#     if_exists='replace',
#     index=False,
#     chunksize=500,
#     dtype={
#         "Username": String(500),
#         "Timezone": String(500),
#         "UTC start": DateTime,
#         "UTC end":  DateTime,
#         "Number": String(500),
#         "CreatedUTC": DateTime
#     }
# )

# table_df = pd.read_sql_table(
#     table_name,
#     con=engine
# )

# print(table_df.head())

"""
Why: there is a limit on the scalability of the architecture in the google spreadsheet. 

It is necessary to exclude all the code for working with Google spreadsheet and replace it with working with a database (PostgreSQL).
Prepare function Init which will automatically migrate data from the current table structure to a new one do not miss existing data.
As result, changes should make a backup of the data, create a new database with a new structure, and upload data from the backup.
"""

# open all sheets and loop through printing each one
# available_sheets = client.openall()
# print([i for i in available_sheets])


# dataframe_list = []
# for i in available_sheets:
#     dataframe = pd.DataFrame(i.get_all_records())
#     dataframe_list.append(dataframe)
# print([i for i in dataframe_list])

