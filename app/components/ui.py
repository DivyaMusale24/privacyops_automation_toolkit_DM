import streamlit as st

def show_dashboard():
    tab1, tab2, tab3 = st.tabs(["Vendor Risk", "RoPA / PIA", "Reports"])

    with tab1:
        st.subheader("Vendor Risk Assessment")
        st.write("Upload and automate third-party risk assessments here.")

    with tab2:
        st.subheader("Records of Processing Activities (RoPA) / Privacy Impact Assessments (PIA)")
        st.write("Generate and maintain RoPA / PIA documentation with ease.")

    with tab3:
        st.subheader("Privacy Reports")
        st.write("View compliance summaries and audit-ready reports.")
