import streamlit as st
from PyPDF2 import PdfReader
from extractor import extract_invoice_data

st.set_page_config(page_title="AI Document Orchestrator")

st.title("📄 AI Document Orchestrator")

uploaded_file = st.file_uploader(
    "Upload Invoice PDF",
    type=["pdf"]
)

def extract_text_from_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📜 Extracted PDF Text")

    st.write(text[:2000])

    if st.button("🚀 Extract Data"):

        with st.spinner("Processing invoice..."):

            result = extract_invoice_data(text)

        st.subheader("🧠 AI Extracted Data")

        st.code(result)