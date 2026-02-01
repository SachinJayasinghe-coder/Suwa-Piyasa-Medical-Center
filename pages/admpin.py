import streamlit as st
import uuid
from database import conn
from datetime import date

st.title("🛠️ Admin / Doctor Panel")

st.subheader("📋 All Appointments")
st.table(conn.execute("SELECT appointment_no, name, date FROM appointments").fetchall())

st.subheader("🩺 Add Medical Record")
u = st.text_input("Patient Username")
n = st.text_area("Doctor Notes")

if st.button("Save Record"):
    conn.execute(
        "INSERT INTO records VALUES (NULL, ?, ?, ?)",
        (u, n, str(date.today()))
    )
    conn.commit()
    st.success("Record saved")

st.subheader("🚶 Physical Booking")
name = st.text_input("Walk-in Patient Name")

if st.button("Generate Appointment Number"):
    app_no = f"SP-{uuid.uuid4().hex[:8].upper()}"
    conn.execute(
        "INSERT INTO appointments (appointment_no, name) VALUES (?, ?)",
        (app_no, name)
    )
    conn.commit()
    st.success(f"Appointment Number: {app_no}")
