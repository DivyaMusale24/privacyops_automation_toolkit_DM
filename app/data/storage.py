import os
import sqlite3
import streamlit as st

DB_PATH = "data/privacyops.db"

def init_db():
    """
    Initializes the SQLite database and creates required tables if they don't exist.
    """
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table for vendor risk assessments
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            risk_level TEXT,
            assessment_date TEXT
        )
    ''')

    # Create table for RoPA / PIA documentation
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ropa_pia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            process_name TEXT NOT NULL,
            data_categories TEXT,
            legal_basis TEXT,
            last_reviewed TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_uploaded_file(uploaded_file, folder):
    """
    Saves an uploaded file to the specified folder within the project.
    Creates the folder if it doesn't exist.
    """
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File '{uploaded_file.name}' saved to {folder}.")

