import requests
import json
from pprint import pprint
from env import notion_access_token ,database_id

url = f"https://api.notion.com/v1/pages"
headers = {
          'Authorization': 'Bearer ' + notion_access_token,
            'Notion-Version': '2021-05-13',
              'Content-Type': 'application/json',
        }
body = {
  'parent': {
      'database_id': database_id,
    },
  'properties':{
    '名前':{
      'title': [
          {
            'text': {
              'content': "test title2"
            }
          }
        ]
    },
    'タグ':{
      "multi_select": [
        {
          'name': 'test tag'
        }
      ]
    },
    'URL':{
      'url': 'https://developers.notion.com/reference/post-page'
    }
  }
}
r = requests.post(url, headers=headers, data=json.dumps(body))

pprint(r.json(), sort_dicts=False)
