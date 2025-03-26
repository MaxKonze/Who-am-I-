import api
import json
import os

class Controller():
    def __init__(self):
        self.game = ""
        self.api = None
        self.load_api()
        self.intial_prompt_ai = (
            "Think of a famous person, either real or fictional. This person can be from any field, including movies, TV, "
            "music, literature, history, or any other area of public interest. Your task is to respond to user questions "
            "about the character you are thinking of. You should only answer each question with either 'Yes' or 'No', and "
            "your answers should be logical and consistent with the character's attributes. Note that you should not answer "
            "the question 'Who are you' or reveal the character's identity directly. Instead, you should allow the user to "
            "guess who the character is through a series of questions.\n\n"
            "**Important Rule:** You must choose a character beforehand and stick to it, without changing or adjusting the "
            "character based on the user's questions. Your answers should be based solely on the characteristics of the "
            "pre-chosen person. In the first answer you are committed to tell me the character's name.\n\n"
            "Go ahead and ask your first question! \n\n"
            "PLease only answer in english."
        )
        
    def load_api(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "config.json")
        with open(config_path, "r") as file:
            config = json.load(file)
        self.api_key = config["API-KEY"]
        self.url = config["API-URL"]
        
        self.api = api.ChatAPI(self.api_key, self.url)

    def start_game(self, game_type):
        if game_type == "AI":
            self.game = "AI"
            self.api.send_message(self.intial_prompt_ai)
            return(self.api.send_message("Let's start the game!"))            
        else:
            self.game = "Player"
    
    def play_game(self, prompt):
        if self.game == "AI":
            self.ai_game(prompt)
        else:
            self.player_game(prompt)
    
    def ai_game(self, prompt):
        response = self.api.send_message(prompt)
        return response
        
    def player_game(self):
        pass
        
    def reset_game(self):
        self.game = ""