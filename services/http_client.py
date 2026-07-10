import requests


class HttpClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get(self, endpoint: str, params: dict | None = None, headers: dict | None = None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers)

    def post(self, endpoint: str, json: dict | None = None, headers: dict | None = None):
        return requests.post(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def put(self, endpoint: str, json: dict | None = None, headers: dict | None = None):
        return requests.put(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def delete(self, endpoint: str, headers: dict | None = None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)
