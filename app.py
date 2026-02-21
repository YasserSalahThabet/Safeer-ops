import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Safeer Operations",
    layout="wide"
)

# Header
col1, col2 = st.columns([1, 5])

with col1:
    st.image("assets/logo.png", width=120)

with col2:
    st.markdown("""
    <h1 style='margin-bottom:0;'>Safeer Operations</h1>
    <p style='color:gray;'>Workforce Scheduling & Attendance Management</p>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
### Platform Overview

This system manages:

• Weekly shift coverage (7-day planning)  
• Automated driver assignment  
• Daily attendance tracking (3 shifts per day)  
• 90-day attendance retention & export  

Use the sidebar to navigate between modules.
""")
