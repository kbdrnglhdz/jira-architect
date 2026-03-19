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

def get_all_fields():
    url = f"{JIRA_URL}/rest/api/3/field/search?query=WS:"
    response = requests.get(url, headers=HEADERS, auth=AUTH)
    return {f['name']: f['id'] for f in response.json().get('values', [])}

def get_all_screens():
    url = f"{JIRA_URL}/rest/api/3/screens"
    params = {"maxResults": 100}
    response = requests.get(url, headers=HEADERS, auth=AUTH, params=params)
    return {s['name']: s['id'] for s in response.json().get('values', []) if s['name'].startswith('WS:')}

def get_first_tab(screen_id):
    url = f"{JIRA_URL}/rest/api/3/screens/{screen_id}/tabs"
    response = requests.get(url, headers=HEADERS, auth=AUTH)
    tabs = response.json()
    if tabs:
        return tabs[0]['id']
    return None

def add_field_to_tab(screen_id, tab_id, field_id):
    url = f"{JIRA_URL}/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields"
    payload = json.dumps({"fieldId": field_id})
    response = requests.post(url, data=payload, headers=HEADERS, auth=AUTH)
    if response.status_code in [200, 201]:
        print(f"Successfully added field {field_id} to screen {screen_id} tab {tab_id}")
    else:
        print(f"Failed to add field to tab: {response.text}")

def main():
    print("Fetching fields...")
    fields = get_all_fields()
    print("Fields:", fields)
    
    print("Fetching screens...")
    screens = get_all_screens()
    print("Screens:", screens)
    
    epic_feature_screen_id = screens.get("WS: SAFe Epic/Feature Create/Edit Screen")
    if epic_feature_screen_id:
        tab_id = get_first_tab(epic_feature_screen_id)
        if tab_id:
            for fname in ["WS: WSJF", "WS: T-Shirt Size"]:
                if fname in fields:
                    add_field_to_tab(epic_feature_screen_id, tab_id, fields[fname])
    
    story_screen_id = screens.get("WS: SAFe Story Create/Edit Screen")
    if story_screen_id:
        tab_id = get_first_tab(story_screen_id)
        if tab_id:
            for fname in ["WS: Story Points", "WS: PI", "WS: DoR Met"]:
                if fname in fields:
                    add_field_to_tab(story_screen_id, tab_id, fields[fname])
                    
    transition_screen_id = screens.get("WS: Transition Screen - DoR Validation")
    if transition_screen_id:
        tab_id = get_first_tab(transition_screen_id)
        if tab_id:
            if "WS: DoR Met" in fields:
                add_field_to_tab(transition_screen_id, tab_id, fields["WS: DoR Met"])
                
    print("Mapping complete!")

if __name__ == "__main__":
    main()
