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

if st.button("Deploy Scheduler"):
    st.success("Scheduler integration will be connected next.")
