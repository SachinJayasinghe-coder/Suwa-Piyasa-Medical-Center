import streamlit as st
from database import conn

st.markdown("""
<style>
html, body, .stApp {
    background: linear-gradient(135deg, #e0f7fa, #f1f8e9) !important;
}
.card {
    background: rgba(255,255,255,0.95);
    padding: 35px;
    border-radius: 22px;
    box-shadow: 0 18px 45px rgba(0,0,0,0.12);
}
</style>
""", unsafe_allow_html=True)

if "user" not in st.session_state:
    st.switch_page("pages/auth.py")

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title(f"Welcome, {st.session_state.user}")

records = conn.execute(
    "SELECT notes,date FROM records WHERE username=?",
    (st.session_state.user,)
).fetchall()

st.subheader("🩺 Medical Records")
for r in records:
    st.info(f"{r[1]} : {r[0]}")

st.button("📅 Book Appointment", use_container_width=True,
          on_click=lambda: st.switch_page("pages/appointment.py"))
st.markdown("</div>", unsafe_allow_html=True)
