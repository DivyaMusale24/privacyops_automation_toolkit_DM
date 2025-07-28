import streamlit as st
from app.components.ui import show_dashboard
from app.data.storage import save_uploaded_file

st.set_page_config(page_title="PrivacyOps Automation Toolkit", layout="wide")

st.title("🛡️ PrivacyOps Automation Toolkit")
st.markdown("Automate vendor risk, RoPA & PIA tracking, and privacy reporting.")

# Define tabs
tab1, tab2, tab3 = st.tabs(["📁 Vendor Risk", "📝 RoPA / PIA", "📊 Reports"])

# Vendor Risk tab
with tab1:
    st.subheader("Vendor Risk Assessment")
    uploaded_file = st.file_uploader("Upload your vendor risk file (.csv or .xlsx):", type=["csv", "xlsx"])
    if uploaded_file:
        save_uploaded_file(uploaded_file, "data/vendor_risk")
    
# RoPA / PIA tab
with tab2:
    st.subheader("RoPA / PIA Documentation")
    uploaded_file = st.file_uploader("Upload your RoPA/PIA file (.csv or .xlsx):", type=["csv", "xlsx"], key="ropa")
    if uploaded_file:
        save_uploaded_file(uploaded_file, "data/ropa_pia")

# Reports tab
with tab3:
    show_dashboard()

