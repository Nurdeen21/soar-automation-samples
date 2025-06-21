"""
slack-notify.py

Send a message to Slack from a SOAR automation script.
"""

import requests

def send_slack_message(webhook_url, message):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    return response.status_code

# Example usage
if __name__ == "__main__":
    print("This is a stub. Replace with your webhook URL and call send_slack_message().")
