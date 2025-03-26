import requests
import json

class API:
    def __init__(self):
        self.url = ""
        self.api_key = ""

        self.load_api()

    def load_api(self):
        # Load data from a JSON file
        with open("config.json", 'r') as file:
            data = json.load(file)
        self.url = data.get("url", "") 
        self.api_key = data.get("api_key", "")

    def send_request(self, data):
        response = requests.post(self.url, headers={"Authorization": self.api_key}, json=data)
        return response.json()