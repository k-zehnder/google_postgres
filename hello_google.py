import os
import gspread
import pandas as pd
from gspread_pandas import Spread, Client
from oauth2client.service_account import ServiceAccountCredentials

"""
# REMINDER: must share email located in key by pressing "share" button in google sheets to share with the credential email or it wont work!
"""

# input
cred_json = os.environ['json_path']

class GooglePostgres:
    def __init__(self, key_path):
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.key_path = key_path

    def googlesheetToPostgres(cred_json, spreadsheetName, sheetName, db_object):
        pass

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



# open all sheets and loop through printing each one
# available_sheets = client.openall()
# print([i for i in available_sheets])


# dataframe_list = []
# for i in available_sheets:
#     dataframe = pd.DataFrame(i.get_all_records())
#     dataframe_list.append(dataframe)
# print([i for i in dataframe_list])

