import requests

def trigger_workflow(data):
    webhook_url = "PASTE_N8N_WEBHOOK_URL"
    return requests.post(webhook_url, json=data).status_code