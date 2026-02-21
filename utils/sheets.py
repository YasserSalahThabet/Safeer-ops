import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

def get_client(service_account_info: dict):
    credentials = Credentials.from_service_account_info(
        service_account_info,
        scopes=SCOPES
    )
    return gspread.authorize(credentials)

def read_sheet(gc, spreadsheet_name: str, worksheet_name: str):
    try:
        sh = gc.open(spreadsheet_name)
        ws = sh.worksheet(worksheet_name)
        data = ws.get_all_records()
        return pd.DataFrame(data)
    except Exception:
        return pd.DataFrame()

def write_sheet(gc, spreadsheet_name: str, worksheet_name: str, df: pd.DataFrame):
    sh = gc.open(spreadsheet_name)

    try:
        ws = sh.worksheet(worksheet_name)
    except:
        ws = sh.add_worksheet(title=worksheet_name, rows="1000", cols="20")

    ws.clear()
    ws.update([df.columns.values.tolist()] + df.values.tolist())
