import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Safeer Operations", layout="wide")

def img_exists(p: str) -> bool:
    return Path(p).exists()

# --- HERO BANNER (only one big image) ---
if img_exists("assets/hero.png"):
    st.image("assets/hero.png", use_container_width=True)

# --- HEADER ROW (logo + title) ---
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
left, right = st.columns([1, 8], vertical_alignment="center")

with left:
    if img_exists("assets/logo.png"):
        st.image("assets/logo.png", width=90)

with right:
    st.markdown(
        """
        <h1 style="margin:0;">Safeer Operations</h1>
        <p style="margin:4px 0 0 0; color:#9CA3AF;">
            Workforce Scheduling & Attendance Management
        </p>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --- KPI CARDS ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Planning Window", "7 Days")
c2.metric("Shifts", "3 / Day")
c3.metric("Attendance Retention", "90 Days")
c4.metric("Data Store", "Google Sheets")

st.markdown(
    """
**Navigation**
- **Coverage**: enter weekly shifts needing coverage + run scheduler  
- **Schedule Attendance**: view results + mark daily attendance  
"""
)
