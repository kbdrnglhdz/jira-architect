import os
import requests
from dotenv import load_dotenv

load_dotenv()
JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

AUTH = (JIRA_USERNAME, JIRA_API_TOKEN)
HEADERS = {"Accept": "application/json"}

url = f"{JIRA_URL}/rest/api/3/project/WS"
response = requests.get(url, headers=HEADERS, auth=AUTH)
if response.status_code == 200:
    proj = response.json()
    types = [it['name'] for it in proj.get('issueTypes', [])]
    print(f"WS Valid Issue Types: {types}")
else:
    print(response.text)
