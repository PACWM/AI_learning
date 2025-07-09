# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv
import json

# these expect to find a .env file at the directory above the lesson.                                                         # the format for that file is (without the comment)                                                                           # API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def save_world(world, filename):
    with open(filename, 'w') as f:
        json.dump(world, f)

def load_world(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def get_together_api_key():
     load_env()
     together_api_key = os.getenv("TOGETHER_API_KEY")
     return together_api_key

def get_azure_openai_config():
    load_env()
    return {
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
        "deployment": os.getenv("AZURE_OPENAI_DEPLOYMENT", "o4-mini")
    }