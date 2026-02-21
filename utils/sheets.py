import pandas as pd
import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

def get_client():
    credentials = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )
    return gspread.authorize(credentials)

def read_sheet(spreadsheet_name: str, worksheet_name: str):
    gc = get_client()
    try:
        sh = gc.open(spreadsheet_name)
        ws = sh.worksheet(worksheet_name)
        data = ws.get_all_records()
        return pd.DataFrame(data)
    except Exception:
        return pd.DataFrame()

def write_sheet(spreadsheet_name: str, worksheet_name: str, df: pd.DataFrame):
    gc = get_client()
    sh = gc.open(spreadsheet_name)

    try:
        ws = sh.worksheet(worksheet_name)
    except:
        ws = sh.add_worksheet(title=worksheet_name, rows="1000", cols="20")

    ws.clear()
    ws.update([df.columns.values.tolist()] + df.values.tolist())
