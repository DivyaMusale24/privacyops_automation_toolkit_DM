import streamlit as st
from app.components.ui import show_dashboard
from app.data.storage import init_db

def main():
    st.set_page_config(page_title="PrivacyOps Automation Toolkit", layout="wide")
    st.title("PrivacyOps Automation Toolkit by DM")
    st.markdown("Automate vendor risk, RoPA & PIA tracking, and privacy reporting.")
    init_db()
    show_dashboard()

if __name__ == "__main__":
    main()
