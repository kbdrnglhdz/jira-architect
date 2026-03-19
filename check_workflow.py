import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

AUTH = (JIRA_USERNAME, JIRA_API_TOKEN)
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def get_project_workflow_scheme(project_key):
    url = f"{JIRA_URL}/rest/api/3/project/{project_key}"
    response = requests.get(url, headers=HEADERS, auth=AUTH)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get project: {response.text}")
        return None

def get_workflows():
    # Fetch paginated workflows
    url = f"{JIRA_URL}/rest/api/3/workflow/search?isActive=true&expand=transitions,statuses"
    response = requests.get(url, headers=HEADERS, auth=AUTH)
    return response.json()

def main():
    print("Fetching project WS...")
    proj = get_project_workflow_scheme("WS")
    if proj:
        # Actually workflow schemes are complex to get from project endpoint in v3, we need to get the issues types or statuses
        print("Project exists.")
    
    print("\nFetching active workflows...")
    wfs = get_workflows()
    for wf in wfs.get('values', []):
        name = wf.get('id', {}).get('name', 'Unknown')
        print(f"Workflow: {name}")

if __name__ == "__main__":
    main()
