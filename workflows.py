import streamlit as st
import requests

def trigger_workflow(data):
    webhook_url = st.secrets["WEBHOOK_URL"]
    return requests.post(webhook_url, json=data).status_code