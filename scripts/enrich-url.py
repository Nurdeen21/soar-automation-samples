"""
enrich-url.py

Simple script stub to query a threat intel API for URL reputation.
"""

import requests

def query_virustotal(url, api_key):
    vt_url = f"https://www.virustotal.com/api/v3/urls/{url}"
    headers = {"x-apikey": api_key}
    response = requests.get(vt_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code}

# Example usage
if __name__ == "__main__":
    print("This is a stub. Replace with your API key and logic.")
