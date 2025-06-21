"""
extract-iocs.py

Helper script to extract indicators of compromise (IOCs) such as URLs, hashes, and IPs from text (e.g., email body).

Intended for use in SOAR playbooks for Splunk SOAR, XSOAR, etc.
"""

import re

def extract_urls(text):
    url_pattern = r'(https?://[^\s]+)'
    return re.findall(url_pattern, text)

# Example usage
if __name__ == "__main__":
    sample_text = "Suspicious link: http://malicious.com/test and https://bad.com/phish"
    urls = extract_urls(sample_text)
    print("Found URLs:", urls)
