import sqlite3
import os

DB_PATH = "suwapiyasa.db"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

# ---------------- USERS ----------------
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    contact TEXT,
    password TEXT
)
""")

# ---------------- APPOINTMENTS ----------------
c.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_no TEXT UNIQUE,

    full_name TEXT,
    age INTEGER,
    gender TEXT,
    contact TEXT,
    email TEXT,

    appointment_date TEXT,
    preferred_time TEXT,
    reason TEXT,
    medical_conditions TEXT,

    document TEXT
)
""")

# ---------------- MEDICAL RECORDS ----------------
c.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    notes TEXT,
    date TEXT
)
""")

# ---------------- LIVE STATUS ----------------
c.execute("""
CREATE TABLE IF NOT EXISTS live_status (
    id INTEGER PRIMARY KEY,
    current_patient INTEGER,
    available INTEGER
)
""")

# Initialize live status safely
c.execute("""
INSERT OR IGNORE INTO live_status (id, current_patient, available)
VALUES (1, 0, 1)
""")

conn.commit()
