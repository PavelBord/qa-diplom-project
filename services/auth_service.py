from services.http_client import HttpClient

BASE_URL = "http://localhost:8000"

class AuthService:
    def __init__(self) -> None:
        self.client = HttpClient(BASE_URL)
    def login(self, email: str, password: str):
        return self.client.post("/auth/login",json={"email": email,"password": password})