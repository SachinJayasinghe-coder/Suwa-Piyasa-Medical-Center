import streamlit as st
from datetime import date

st.set_page_config(page_title="Suwa Piyasa Medical Center", layout="wide")

# 🌈 GLOBAL THEME
st.markdown("""
<style>
html, body, .stApp {
    background: linear-gradient(135deg, #e0f7fa, #f1f8e9) !important;
}
.block-container {
    padding: 1.5rem 2rem;
}
.card {
    background: rgba(255,255,255,0.92);
    padding: 35px;
    border-radius: 22px;
    box-shadow: 0 18px 45px rgba(0,0,0,0.12);
    margin-bottom: 35px;
}
.profile-card {
    background: linear-gradient(135deg, #ffffff, #e0f2f1);
    padding: 40px;
    border-radius: 24px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.15);
    margin-bottom: 35px;
}
.notice-card {
    background: linear-gradient(135deg, #f1f8e9, #ffffff);
    padding: 30px;
    border-radius: 20px;
    border-left: 8px solid #26c6da;
    box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    margin-bottom: 30px;
}
.title {
    text-align: center;
    font-size: 56px;
    font-weight: 800;
    color: #00695c;
}
.subtitle {
    text-align: center;
    font-size: 26px;
    color: #455a64;
}
.stButton > button {
    background: linear-gradient(135deg, #26c6da, #0097a7);
    color: white;
    border-radius: 14px;
    font-size: 16px;
    padding: 12px 20px;
    border: none;
}
.footer {
    text-align: center;
    color: #546e7a;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# 🔝 TOP BAR
c1, c2, c3 = st.columns([6,2,2])
with c2:
    if st.button("Login", use_container_width=True):
        st.switch_page("pages/auth.py")
with c3:
    if st.button("Register", use_container_width=True):
        st.switch_page("pages/auth.py")

# 🏥 HEADER
st.markdown("<div class='title'>Suwa Piyasa</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Medical Center</div>", unsafe_allow_html=True)

# 👨‍⚕️ DOCTOR INTRO BOX
st.markdown("<div class='profile-card'>", unsafe_allow_html=True)
st.subheader("👨‍⚕️ Meet Our Doctor")
st.write("### Dr. Gayan S. Jayasuriya")
st.write("**MBBS No:** 123456")
st.write(
    "Dr. Gayan S. Jayasuriya is a highly experienced and compassionate medical "
    "professional dedicated to ethical, patient-centred healthcare and long-term wellbeing."
)
st.markdown("</div>", unsafe_allow_html=True)

# 📅 APPOINTMENT BUTTON
a,b,c = st.columns([1,2,1])
with b:
    if st.button("📅 Make an Appointment", use_container_width=True):
        st.switch_page("pages/appointment.py")

# 📢 NOTICE BOARD BOX
st.markdown("<div class='notice-card'>", unsafe_allow_html=True)
st.subheader("📢 Notice Board")
st.write("🕒 **Consultation Time:** 6.00 PM – 9.00 PM")
st.write("📅 **Closed:** Poya Days")
st.write("🧪 **New:** Laboratory services available")
st.markdown("</div>", unsafe_allow_html=True)

# 👥 OUR TEAM
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("👥 Our Team")
st.write("👨‍⚕️ Doctor – Dr. Gayan S. Jayasuriya")
st.write("👩‍⚕️ Nurse – Registered Nursing Officer")
st.write("🧾 Receptionist – Patient Care Assistant")
st.markdown("</div>", unsafe_allow_html=True)

# 🔻 FOOTER
st.markdown(
    f"<div class='footer'>Developed by <b>Sachin Jayasinghe</b><br>{date.today()}</div>",
    unsafe_allow_html=True
)
