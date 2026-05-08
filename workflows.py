import requests

def trigger_workflow(data):
    webhook_url = "https://tinapawar.app.n8n.cloud/webhook/584f8697-11f6-4ccd-9752-a62221c63555"
    return requests.post(webhook_url, json=data).status_code