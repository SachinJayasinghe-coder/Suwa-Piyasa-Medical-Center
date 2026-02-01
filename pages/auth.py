import streamlit as st
import hashlib
from database import conn

def hash_pw(p): return hashlib.sha256(p.encode()).hexdigest()

st.markdown("""
<style>
html, body, .stApp {
    background: linear-gradient(135deg, #e0f7fa, #f1f8e9) !important;
}
.auth-card {
    max-width: 420px;
    margin: auto;
    background: rgba(255,255,255,0.95);
    padding: 40px;
    border-radius: 24px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
st.title("👤 Patient Access")

mode = st.radio("Choose Option", ["Login", "Register"])

if mode == "Register":
    full_name = st.text_input("Full Name")
    username = st.text_input("Username")
    email = st.text_input("Email")
    contact = st.text_input("Contact Number")
    password = st.text_input("Password", type="password")

    if st.button("Create Account", use_container_width=True):
        conn.execute(
        """
        INSERT INTO users (username, full_name, email, contact, password)
        VALUES (?, ?, ?, ?, ?)
        """,
        (username, full_name, email, contact, hash_pw(password)))
        conn.commit()
        st.success("Account created successfully")

else:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, hash_pw(password))
        ).fetchone()

        if user:
            st.session_state.user = username
            st.switch_page("pages/patient_dashboard.py")
        else:
            st.error("Invalid credentials")

st.markdown("</div>", unsafe_allow_html=True)
