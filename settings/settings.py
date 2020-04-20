from dotenv import load_dotenv
import os

class Settings():
    def __init__(self):
        load_dotenv()
    
    def get_api_token(self):
        return os.getenv('INSTAGRAM_TOKEN')