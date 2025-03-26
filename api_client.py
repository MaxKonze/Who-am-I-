import api
import requests
import json

class API:
    def __init__(self):
        self.url = ""
        self.api_key = ""
        self.response = ""
        
        self.header = {
            "Authorization": ""
        }
        
        self.body = {
            "model": "1 - Llama3 405 on WestAI with 4b quantization",
            "prompt": "hello how r u ?", 
            "temperature": 0.7, 
            "n": 1,
            "max_tokens": 16,
            "stream": False,
            "top_p": 1,
            "top_k": -1,
            "logprobs": 0,
            "echo": False,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "user": "string",
            "use_beam_search":"False",
            "best_of": 0 
        }        

        self.load_api() 
        
    
    def edit_body(self, prompt, model):
        self.body["prompt"] = prompt
        
        if model != None:
            self.body["model"] = model
        
    
    def format_response(self):
        return self.response["choices"]["text"]
    
    def load_api(self):
        with open("config.json", "r") as file:
            config = json.load(file)
        self.api_key = config["APi-Key"]
        self.header["Authorization"] = f"Bearer {self.api_key}" 
    
    
    def send_request(self, prompt):
        self.edit_body(prompt, None)
        print(self.url)
        response = requests.post(self.url, headers=self.header, json=self.body)
        self.response = response.json()
        
        self.formatted_response = self.format_response()
        
        return self.formatted_response
        
        
       