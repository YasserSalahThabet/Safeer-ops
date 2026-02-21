import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Safeer Operations", layout="wide")

def show_image(path: str, width: int | None = None):
    p = Path(path)
    if p.exists():
        st.image(str(p), width=width, use_container_width=(width is None))
        return True
    return False

# --- HERO (full width) ---
# Put your best wide banner as assets/hero.png
show_image("assets/hero.png", width=None)

# --- HEADER ---
st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1.2, 6, 1.2])

with c2:
    # Bigger logo centered
    logo_exists = show_image("assets/logo.png", width=220)
    if not logo_exists:
        st.warning("Logo not found (assets/logo.png).")

    st.markdown(
        """
        <h1 style="text-align:center; margin: 0;">Safeer Operations</h1>
        <p style="text-align:center; color: #9CA3AF; margin-top: 6px;">
            Workforce Scheduling & Attendance Management
        </p>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --- OVERVIEW CARDS ---
st.markdown("## Platform Overview")

colA, colB, colC, colD = st.columns(4)

with colA:
    st.metric("Planning", "7 Days", "Weekly Coverage")
with colB:
    st.metric("Shifts", "3 / Day", "Daily Operations")
with colC:
    st.metric("Attendance", "90 Days", "Retention")
with colD:
    st.metric("Drivers", "Master List", "IDs + Status")

st.markdown(
    """
    Use the sidebar to navigate:
    - **Coverage**: input weekly shifts needing coverage + run scheduler  
    - **Schedule Attendance**: view results + mark attendance daily  
    """
)
