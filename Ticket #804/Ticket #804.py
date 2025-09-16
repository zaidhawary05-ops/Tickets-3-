import requests
import os
from dotenv import load_dotenv

API_KEY = os.getenv("API_KEY")

def get_data(city):
    return requests.get(f"https://api.example.com/{city}?key={API_KEY}").json()

