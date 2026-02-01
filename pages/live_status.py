import streamlit as st
from database import conn

st.title("🔴 Live Doctor Status")

status = conn.execute("SELECT * FROM live_status").fetchone()

if status[2] == 1:
    st.success(f"Doctor Available | Currently seeing patient #{status[1]}")
else:
    st.error("Doctor Not Available")

st.subheader("Admin Control")
available = st.checkbox("Doctor Available", value=bool(status[2]))
current = st.number_input("Current Patient Number", min_value=0, value=status[1])

if st.button("Update Status"):
    conn.execute(
        "UPDATE live_status SET current_patient=?, available=? WHERE id=1",
        (current, int(available))
    )
    conn.commit()
    st.success("Live status updated")
