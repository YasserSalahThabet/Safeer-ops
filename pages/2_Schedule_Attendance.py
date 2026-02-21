import streamlit as st
from pathlib import Path
import datetime

st.set_page_config(page_title="Attendance | Safeer Ops", layout="wide")

def img_exists(p):
    return Path(p).exists()

# --- HERO BANNER ---
if img_exists("assets/attendance.png"):
    st.image("assets/attendance.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- PAGE HEADER ---
st.markdown(
    """
    <h1 style='margin-bottom:0;'>Shift Attendance</h1>
    <p style='color:#9CA3AF; margin-top:5px;'>
        Supervisor role management • Daily tracking • 90-day retention
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- DATE + SHIFT SELECTOR ---
col1, col2 = st.columns([2,2])

with col1:
    selected_date = st.date_input(
        "Select Date",
        value=datetime.date.today(),
        format="DD/MM/YYYY"
    )

with col2:
    shift = st.selectbox(
        "Select Shift",
        ["Morning", "Afternoon", "Night"]
    )

st.markdown("### Drivers on Shift")

# Placeholder table (we’ll connect logic next)
st.dataframe(
    {
        "Driver ID": [],
        "Driver Name": [],
        "Status": []
    },
    use_container_width=True
)

st.markdown("---")

# Small subtle footer (not loud)
st.markdown(
    """
    <p style='font-size:12px; color:#6B7280;'>
    Safeer Operations • Attendance Module
    </p>
    """,
    unsafe_allow_html=True
)
