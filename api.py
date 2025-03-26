import requests

class ChatAPI:
    def __init__(self, key, url):
        """
        Initializes the ChatAPI with the API key and URL.
        """
        self.model = "1 - Llama3 405 on WestAI with 4b quantization"
        self.key = key
        self.url = url
        self.chat_history = [
            {"role": "system", "content": "Du bist ein hilfreicher Assistent."}
        ]

    def send_message(self, user_input):
        """
        Sends a message to the API and stores the response.
        """
        # Add the user's message to the chat history
        self.chat_history.append({"role": "user", "content": user_input})

        # Prepare the request
        headers = {"Authorization": f"Bearer {self.key}", "Content-Type": "application/json"}
        payload = {
            "model": self.model,
            "messages": self.chat_history,
            "max_tokens": 100,
            "temperature": 1,
            "top_p": 1,
            "n": 1,
        }

        # Send the request
        response = requests.post(self.url, headers=headers, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            assistant_reply = response_data["choices"][0]["message"]["content"]
            print(f"Assistent: {assistant_reply}")

            # Save the assistant's reply in the chat history
            self.chat_history.append({"role": "assistant", "content": assistant_reply})

            # Optionally truncate the chat history if it gets too long
            if len(self.chat_history) > 100:
                self.chat_history = [self.chat_history[0]] + self.chat_history[-9:]
                
            return assistant_reply
        else:
            print("Fehler bei der Anfrage:", response.text)