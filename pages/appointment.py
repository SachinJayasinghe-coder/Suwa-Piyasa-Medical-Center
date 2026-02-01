import streamlit as st
import uuid
from database import conn
from pdf_generator import generate_pdf

# 🌈 GLOBAL THEME (SAME AS OTHER PAGES)
st.markdown("""
<style>
html, body, .stApp {
    background: linear-gradient(135deg, #e0f7fa, #f1f8e9) !important;
}
.card {
    background: rgba(255,255,255,0.95);
    padding: 40px;
    border-radius: 24px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.15);
    max-width: 720px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("📋 Make an Appointment")

# ---------------- PATIENT INFORMATION ----------------
st.subheader("👤 Patient Information")
full_name = st.text_input("Full Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
contact = st.text_input("Contact Number")
email = st.text_input("Email Address")

st.divider()

# ---------------- APPOINTMENT DETAILS ----------------
st.subheader("🏥 Appointment Details")
appointment_date = st.date_input("Appointment Date")
preferred_time = st.selectbox(
    "Preferred Time",
    ["Select", "Morning", "Afternoon", "Evening"]
)
reason = st.text_area("Reason for Visit")
medical_conditions = st.text_area(
    "Existing Medical Conditions (if any)",
    placeholder="Diabetes, blood pressure, allergies, etc."
)

st.divider()

# ---------------- DOCUMENT UPLOAD ----------------
st.subheader("📎 Upload Documents")
document = st.file_uploader(
    "Upload medical reports / prescriptions (optional)",
    type=["pdf", "jpg", "png"]
)

# ---------------- SUBMIT ----------------
if st.button("Confirm Appointment", use_container_width=True):
    if not full_name or not contact or gender == "Select" or preferred_time == "Select" or not reason:
        st.error("Please fill all required fields")
    else:
        # Generate UNIQUE appointment number
        appointment_no = f"SP-{uuid.uuid4().hex[:8].upper()}"

        # Save document
        document_path = None
        if document:
            document_path = f"uploads/{document.name}"
            with open(document_path, "wb") as f:
                f.write(document.getbuffer())

        # Insert into database
        conn.execute(
            """
            INSERT INTO appointments (
                appointment_no,
                full_name,
                age,
                gender,
                contact,
                email,
                appointment_date,
                preferred_time,
                reason,
                medical_conditions,
                document
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                appointment_no,
                full_name,
                age,
                gender,
                contact,
                email,
                str(appointment_date),
                preferred_time,
                reason,
                medical_conditions,
                document_path
            )
        )
        conn.commit()

        # Generate PDF
        pdf_file = f"{appointment_no}.pdf"
        generate_pdf(pdf_file, appointment_no, full_name, appointment_date)

        st.success("✅ Appointment booked successfully!")
        st.write(f"**Your Appointment Number:** `{appointment_no}`")

        st.download_button(
            "📄 Download Appointment PDF",
            open(pdf_file, "rb"),
            file_name=pdf_file
        )

st.markdown("</div>", unsafe_allow_html=True)
