import streamlit as st
import pandas as pd

st.title("Schedule & Attendance")

st.markdown("### Today's Operations")

st.info("Scheduled drivers will appear here after scheduler integration.")

st.markdown("---")

st.markdown("### Attendance Marking")

attendance_columns = [
    "slot_id",
    "driver_id",
    "status",
    "check_in",
    "check_out",
    "notes"
]

if "attendance_df" not in st.session_state:
    st.session_state.attendance_df = pd.DataFrame(columns=attendance_columns)

edited_attendance = st.data_editor(
    st.session_state.attendance_df,
    num_rows="dynamic",
    use_container_width=True
)

st.session_state.attendance_df = edited_attendance

st.markdown("---")

if st.button("Export Attendance (CSV)"):
    csv = st.session_state.attendance_df.to_csv(index=False)
    st.download_button(
        "Download File",
        csv,
        file_name="attendance_export.csv",
        mime="text/csv"
    )
