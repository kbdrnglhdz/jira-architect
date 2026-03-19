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

def get_issue_types():
    response = requests.get(f"{JIRA_URL}/rest/api/3/issuetype", headers=HEADERS, auth=AUTH)
    if response.status_code == 200:
        return {it["name"]: it["id"] for it in response.json()}
    return {}

def create_issue_type(name, description, type_level=0):
    url = f"{JIRA_URL}/rest/api/3/issuetype"
    payload = json.dumps({
        "name": name,
        "description": description
    })
    response = requests.post(url, data=payload, headers=HEADERS, auth=AUTH)
    if response.status_code == 201:
        print(f"Created Issue Type: {name}")
        return response.json()['id']
    else:
        print(f"Failed to create Issue Type {name}: {response.text}")
    return None

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
    print("--- Enforcing ITIL Schema on Jira ---")
    
    # Check Issue type
    issue_types = get_issue_types()
    itil_issue_type = "Incidente de Producción"
    if itil_issue_type not in issue_types:
        create_issue_type(itil_issue_type, "Gestión de incidentes de producción ITIL")
    else:
        print(f"Issue Type '{itil_issue_type}' already exists.")

    print("\n--- Creating Custom Fields ---")
    
    fields = [
        {
            "name": "WS: Impacto",
            "desc": "Impacto del incidente en el negocio",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:select",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher"
        },
        {
            "name": "WS: Urgencia",
            "desc": "Urgencia de atención para el incidente",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:select",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher"
        },
        {
            "name": "WS: Servicio Afectado",
            "desc": "Servicio de negocio o técnico afectado",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:textsearcher"
        },
        {
            "name": "WS: SLA Deadline",
            "desc": "Fecha límite de resolución del SLA",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:datetime",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:datetimerange"
        },
        {
            "name": "WS: Workaround",
            "desc": "Solución temporal aplicada al incidente",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:textsearcher"
        },
        {
            "name": "WS: Causa Raíz Inicial",
            "desc": "Causa raíz inicial antes de pasarlo a Problem Management",
            "type": "com.atlassian.jira.plugin.system.customfieldtypes:textarea",
            "searcher": "com.atlassian.jira.plugin.system.customfieldtypes:textsearcher"
        }
    ]
    
    for f in fields:
        create_custom_field(f['name'], f['desc'], f['type'], f['searcher'])

    print("\n--- Creating Screens ---")
    screens_to_create = [
        {"name": "WS: Pantalla de Incidente de Producción", "desc": "Pantalla principal para incidentes"}
    ]
    
    for s in screens_to_create:
        create_screen(s['name'], s['desc'])

    print("\n--- Mapping Fields to Screens ---")
    
    jira_fields = get_all_fields()
    jira_screens = get_all_screens()
    
    screen_id = jira_screens.get("WS: Pantalla de Incidente de Producción")
    if screen_id:
        tab_id = get_first_tab(screen_id)
        if tab_id:
            # Ordenar primero los críticos
            fields_to_add = ["WS: SLA Deadline", "WS: Servicio Afectado", "WS: Impacto", "WS: Urgencia", "WS: Workaround", "WS: Causa Raíz Inicial"]
            for fname in fields_to_add:
                if fname in jira_fields:
                    add_field_to_tab(screen_id, tab_id, jira_fields[fname])
                else:
                    print(f"Warning: Field {fname} not found in fetched fields.")

if __name__ == "__main__":
    main()
