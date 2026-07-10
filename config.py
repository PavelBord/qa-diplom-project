import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
API_URL = os.getenv("API_URL", "http://localhost:8000")

EMAIL = os.getenv("EMAIL", "admin@example.com")
PASSWORD = os.getenv("PASSWORD", "admin123")
