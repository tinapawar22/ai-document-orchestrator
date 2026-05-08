import google.generativeai as genai
import streamlit as st
import json

# Configure Gemini API securely
genai.configure(api_key=st.secrets["AIzaSyAP2xfatGI7bT0m0YEf8hsoJnvmsmIco_U"])

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")


def extract_invoice_data(text):

    prompt = f"""
    You are an intelligent invoice extraction system.

    Extract invoice details from the provided invoice text.

    Return ONLY valid JSON in this exact format:

    {{
        "invoice_number": "",
        "date": "",
        "vendor_name": "",
        "total_amount": null
    }}

    Rules:
    - Return ONLY JSON
    - No markdown
    - No explanation text
    - If a value is missing, return null
    - total_amount must be numeric only
    - Do not include currency symbols

    Invoice Text:
    {text}
    """

    try:
        response = model.generate_content(prompt)

        cleaned_response = response.text.strip()

        # Convert JSON string to Python dictionary
        data = json.loads(cleaned_response)

        return data

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by Gemini",
            "raw_response": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }