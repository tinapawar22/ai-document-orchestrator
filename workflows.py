import requests
import streamlit as st

def trigger_workflow(data):

    webhook_url = st.secrets["WEBHOOK_URL"]

    response = requests.post(
        webhook_url,
        json=data
    )

    return response.status_code