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

def create_custom_field(name, description, field_type, searcher_key):
    url = f"{JIRA_URL}/rest/api/3/field"
    payload = json.dumps({
        "name": name,
        "description": description,
        "type": field_type,
        "searcherKey": searcher_key
    })
    
    response = requests.post(url, data=payload, headers=HEADERS, auth=AUTH)
    if response.status_code == 201:
        print(f"Created custom field: {name}")
        return response.json()['id']
    elif response.status_code == 400 and 'Field with name' in response.text:
       print(f"Custom field '{name}' already exists or bad request: {response.text}")
    else:
        print(f"Failed to create custom field {name}: {response.text}")
    return None


def create_screen(name, description):
    url = f"{JIRA_URL}/rest/api/3/screens"
    payload = json.dumps({
        "name": name,
        "description": description
    })
    
    response = requests.post(url, data=payload, headers=HEADERS, auth=AUTH)
    if response.status_code == 201:
        print(f"Created screen: {name}")
        return response.json()['id']
    else:
        print(f"Failed to create screen {name}: {response.text}")
    return None

def main():
    if not JIRA_URL or not JIRA_USERNAME or not JIRA_API_TOKEN:
        print("Missing variables in .env")
        return

    print("--- Creating Custom Fields ---")
    
    # Custom fields creation
    fields = [
        {
            "name": "WS: WSJF",
            "desc": "Weighted Shortest Job First",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:float",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:exactnumber"
        },
        {
            "name": "WS: T-Shirt Size",
            "desc": "T-Shirt Size Estimation",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:select",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher"
        },
        {
            "name": "WS: Story Points",
            "desc": "Story Points estimation",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:float",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:exactnumber"
        },
        {
            "name": "WS: PI",
            "desc": "Program Increment",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:version",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:versionsearcher"
        },
        {
            "name": "WS: DoR Met",
            "desc": "Definition of Ready Met validation",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher"
        }
    ]
    
    for f in fields:
        create_custom_field(f['name'], f['desc'], f['type'], f['searcher'])

    print("\n--- Creating Screens ---")
    screens = [
        {"name": "WS: SAFe Epic/Feature Create/Edit Screen", "desc": "Screen for Epic and Feature"},
        {"name": "WS: SAFe Story Create/Edit Screen", "desc": "Screen for Story and Enabler"},
        {"name": "WS: Transition Screen - DoR Validation", "desc": "Transition screen requiring DoR validation"}
    ]
    
    for s in screens:
        create_screen(s['name'], s['desc'])


if __name__ == "__main__":
    main()
