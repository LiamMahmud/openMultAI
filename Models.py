import requests


class Models:
    def __init__(self, client):
        self.client = client

    def list(self):
        response = requests.get(f"{self.client.base_url}/list/models")
        return response.json()
