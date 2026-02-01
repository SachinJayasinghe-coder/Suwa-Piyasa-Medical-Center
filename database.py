import sqlite3

conn = sqlite3.connect("suwapiyasa_v2.db", check_same_thread=False)
c = conn.cursor()

# USERS TABLE (5 columns)
c.execute("""
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    contact TEXT,
    password TEXT
)
""")

# APPOINTMENTS TABLE
c.execute("""
CREATE TABLE appointments (
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

# MEDICAL RECORDS
c.execute("""
CREATE TABLE records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    notes TEXT,
    date TEXT
)
""")

# LIVE STATUS
c.execute("""
CREATE TABLE live_status (
    id INTEGER PRIMARY KEY,
    current_patient INTEGER,
    available INTEGER
)
""")

c.execute("INSERT OR IGNORE INTO live_status VALUES (1, 0, 1)")
conn.commit()
