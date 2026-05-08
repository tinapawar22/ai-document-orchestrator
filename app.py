import streamlit as st
from PyPDF2 import PdfReader
from extractor import extract_invoice_data
from workflow import trigger_workflow

# Page configuration
st.set_page_config(page_title="AI Document Orchestrator")

# App title
st.title("📄 AI Document Orchestrator")

# File uploader
uploaded_file = st.file_uploader(
    "Upload Invoice PDF",
    type=["pdf"]
)


# Function to extract text from PDF
def extract_text_from_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


# Main workflow
if uploaded_file:

    # Extract PDF text
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📜 Extracted PDF Text")
    st.write(text[:2000])

    # Button to trigger AI extraction
    if st.button("🚀 Extract Data"):

        # Check if text exists
        if not text.strip():

            st.error("No text found in PDF")

        else:

            with st.spinner("Processing invoice with AI..."):

                # Extract invoice data using Gemini
                result = extract_invoice_data(text)

            # Show extracted JSON
            st.subheader("🧠 AI Extracted Data")
            st.json(result)

            # Trigger n8n workflow
            try:

                status = trigger_workflow(result)

                if status == 200:
                    st.success("✅ n8n Workflow Triggered Successfully!")

                else:
                    st.error(f"❌ Workflow trigger failed. Status code: {status}")

            except Exception as e:

                st.error(f"⚠️ Error triggering workflow: {str(e)}")