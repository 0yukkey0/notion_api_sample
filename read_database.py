import requests
from pprint import pprint
from env import notion_access_token, database_id


url = f"https://api.notion.com/v1/databases/{database_id}/query"
headers = {
    'Authorization': 'Bearer ' + notion_access_token,
    'Notion-Version': '2021-05-13',
    'Content-Type': 'application/json',
}
r = requests.post(url, headers=headers)

pprint(r.json(), sort_dicts=False)
