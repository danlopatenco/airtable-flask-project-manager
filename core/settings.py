import os
from dotenv import load_dotenv

load_dotenv()

FLASK_DEBUG = bool(os.getenv('FLASK_DEBUG'))
FLASK_HOST = os.getenv('FLASK_HOST')
FLASK_PORT = os.getenv('FLASK_PORT')

AIRTABLE_TOKEN = os.getenv('AIRTABLE_TOKEN')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_PROJECTS_TABLE_NAME = os.getenv('AIRTABLE_PROJECTS_TABLE_NAME')
AIRTABLE_TASKS_TABLE_NAME = os.getenv('AIRTABLE_TASKS_TABLE_NAME')
