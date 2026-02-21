import streamlit as st
import pandas as pd

st.title("Coverage Planning")

st.markdown("""
Enter weekly shift coverage requirements.

Each shift requires:
- Date (DD/MM/YYYY)
- Start Time (24h format)
- End Time (24h format)
- Zone
- Required Drivers
""")

columns = ["shift_id", "date", "start_time", "end_time", "zone", "required_drivers"]

if "coverage_df" not in st.session_state:
    st.session_state.coverage_df = pd.DataFrame(columns=columns)

edited = st.data_editor(
    st.session_state.coverage_df,
    num_rows="dynamic",
    use_container_width=True
)

st.session_state.coverage_df = edited

st.markdown("---")

from utils.sheets import write_sheet

if st.button("Save Coverage to Google Sheets"):
    write_sheet("Safeer", "Client_Shifts_Weekly", st.session_state.coverage_df)
    st.success("Coverage saved to Google Sheets.")
