import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.environ.get('MISTRAL_API_KEY')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
