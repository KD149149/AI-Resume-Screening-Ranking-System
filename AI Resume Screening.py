# Developer Information
#
# Developer: Kajal Dadas
# Contact: +91 7972244559
# Email: kajaldadas149@gmail.com
# This project is fully designed and developed by Kajal Dadas.

import streamlit as st
import os
import shutil
import pandas as pd
from PyPDF2 import PdfReader

# ---------------- CONFIG ----------------
UPLOAD_DIR = "uploaded_resumes"
SCREENED_DIR = "screened_resumes"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(SCREENED_DIR, exist_ok=True)

# ---------------- FUNCTIONS ----------------
def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def calculate_score(text, keywords):
    return sum(1 for k in keywords if k in text)

def get_pdfs(folder):
    return [f for f in os.listdir(folder) if f.endswith(".pdf")]

# ---------------- UI ----------------
st.set_page_config("AI Resume Screening", layout="centered")

# ---------- Custom Header ----------
st.markdown("<p style='font-size:14px; color:gray; text-align:center;'>Design Developed by Kajal Dadas</p>", unsafe_allow_html=True)

st.title("🤖 AI Resume Screening & Ranking System")

st.markdown("### Step 1: Enter Screening Keywords")
keywords_input = st.text_area(
    "Keywords (comma separated)",
    placeholder="python, machine learning, sql, deep learning"
)

threshold = st.slider("Minimum Keyword Match Threshold", 1, 10, 3)

st.markdown("---")
st.markdown("### Step 2: Upload Resumes")

uploaded_files = st.file_uploader(
    "Dump resumes here (PDF only)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        path = os.path.join(UPLOAD_DIR, file.name)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(file.read())
    st.success("Resumes uploaded to folder successfully.")

st.markdown("---")

if st.button("🚀 Scan & Screen Resumes"):

    if not keywords_input.strip():
        st.warning("Please enter keywords before screening.")
    else:
        keywords = [k.strip().lower() for k in keywords_input.split(",")]
        results = []

        pdfs = get_pdfs(UPLOAD_DIR)

        for pdf in pdfs:
            pdf_path = os.path.join(UPLOAD_DIR, pdf)
            text = extract_text(pdf_path)
            score = calculate_score(text, keywords)

            status = "Rejected"
            if score >= threshold:
                shutil.move(pdf_path, os.path.join(SCREENED_DIR, pdf))
                status = "Screened"

            results.append({
                "Resume": pdf,
                "Keyword Matches": score,
                "Status": status
            })

        if results:
            df = pd.DataFrame(results).sort_values(
                by="Keyword Matches", ascending=False
            )
            st.success("Screening completed.")
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No resumes found in upload folder.")

st.markdown("---")

# ---------------- Folder Visibility ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📂 Uploaded Resumes")
    uploaded_list = get_pdfs(UPLOAD_DIR)
    if uploaded_list:
        st.write(uploaded_list)
    else:
        st.caption("No resumes pending.")

with col2:
    st.markdown("### ✅ Screened Resumes")
    screened_list = get_pdfs(SCREENED_DIR)
    if screened_list:
        st.write(screened_list)
    else:
        st.caption("No resumes screened yet.")
