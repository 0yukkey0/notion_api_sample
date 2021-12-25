from dotenv import load_dotenv
import os

load_dotenv()

notion_access_token = os.getenv('NOTION_ACCESS_TOKEN')
database_id = os.getenv('NOTION_DATABASE_ID')
