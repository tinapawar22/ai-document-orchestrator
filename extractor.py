import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyADgAQh3GHlrUPYHzhyhwP9usVoIlNnqP8")

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")

def extract_invoice_data(text):

    prompt = f"""
    Extract invoice details from the following text.

    Return ONLY valid JSON.

    {{
        "invoice_number": "",
        "date": "",
        "vendor_name": "",
        "total_amount": ""
    }}

    Invoice Text:
    {text}
    """

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"