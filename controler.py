import api
import json

class Controller():
    def __init__(self):
        self.game = ""
        self.api = None
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
            "Go ahead and ask your first question!"
        )
        
    def load_api(self):
        with open("config.json", "r") as file:
            config = json.load(file)
        self.api_key = config["APi-Key"]
        self.url = config["URL"]
        
        self.api = api.ChatAPI(self.api_key, self.url)

    def start_game(self, game_type):
        if game_type == "AI":
            self.game = "AI"
            api.send_request(self.intial_prompt_ai)
            return(api.send_request("Let's start the game!"))            
        else:
            self.game = "Player"
    
    def play_game(self, prompt):
        if self.game == "AI":
            self.ai_game(prompt)
        else:
            self.player_game(prompt)
    
    def ai_game(self, prompt):
        response = self.api.send_request(prompt)
        return response
        
    def player_game(self):
        pass
        
    def reset_game(self):
        self.game = ""