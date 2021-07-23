# imports from unut
import os
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import datetime

# util.py imports
import os
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import datetime

#cred_json = os.environ['json_path']
cred_json = "/home/batman/Desktop/google_postgres/key/master_key.json" 
class GoogleSheetHelper:
    """Helper claas to pull data from googlesheets"""
    def __init__(self, cred_json, spreadsheetName, sheetName):
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.cred_json = cred_json
        self.spreadsheetName = spreadsheetName
        self.sheetName = sheetName
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(self.cred_json, self.scope)
        self.client = gspread.authorize(self.creds)

    def getDataframe(self):
        """Returns all rows data from sheet as dataframe"""
        spreadsheet = self.client.open(self.spreadsheetName)
        sheet = spreadsheet.worksheet(self.sheetName)
        rows = sheet.get_all_records()
        return pd.DataFrame(rows)

    def getDict(self):
        """Returns all rows data from sheet as dictionary--one dict per row"""        
        spreadsheet = self.client.open(self.spreadsheetName)
        sheet = spreadsheet.worksheet(self.sheetName)
        rows = sheet.get_all_records()
        return rows

    def viewAllClientSheets(self):
        """Returns sheets this gspread (self.client) authorized to view/edit"""
        available_sheets = self.client.openall()
        return [sheet.title for sheet in available_sheets]


df1 = GoogleSheetHelper(cred_json, "google_postgres", "existing")
df2 = GoogleSheetHelper(cred_json, "google_postgres", "calls")
df3 = GoogleSheetHelper(cred_json, "google_postgres", "time")


host = "localhost"
port = 5432
username = "zelda"
password = "password"
database = "test_godo" 

db_uri = f"postgresql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(db_uri, echo=True)


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

"""
Why: there is a limit on the scalability of the architecture in the google spreadsheet. 

It is necessary to exclude all the code for working with Google spreadsheet and replace it with working with a database (PostgreSQL).
Prepare function Init which will automatically migrate data from the current table structure to a new one do not miss existing data.
As result, changes should make a backup of the data, create a new database with a new structure, and upload data from the backup.
"""
"""
# REMINDER: must share email located in key by pressing "share" button in google sheets to share with the credential email or it wont work!
"""
