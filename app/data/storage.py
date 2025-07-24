import sqlite3
import os

DB_PATH = "data/privacyops.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create simple tables to start with
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            risk_level TEXT,
            assessment_date TEXT
        )
    ''')

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
