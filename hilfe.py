import requests
import json

# API-Endpunkt
API_URL = "https://helmholtz-blablador.fz-juelich.de:8000/v1/chat/completions"
API_KEY = "API_KEY"  # Falls erforderlich

# Nachrichtenverlauf
chat_history = [
    {"role": "system", "content": "Du bist ein hilfreicher Assistent."}
]

def send_message(user_input):
    """Sendet eine Nachricht an die API und speichert die Antwort."""
    global chat_history
    
    # Neue Nutzernachricht hinzufügen
    chat_history.append({"role": "user", "content": user_input})
    
    # Anfrage an die API vorbereiten
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "1 - Llama3 405 on WestAI with 4b quantization",
        "messages": chat_history,
        "max_tokens": 100
    }
    
    # Anfrage senden
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        response_data = response.json()
        assistant_reply = response_data["choices"][0]["message"]["content"]
        print(f"Assistent: {assistant_reply}")
        
        # Antwort des Assistenten speichern
        chat_history.append({"role": "assistant", "content": assistant_reply})
        
        # Optional: Chatverlauf kürzen, falls zu lang
        if len(chat_history) > 10:
            chat_history = [chat_history[0]] + chat_history[-9:]
    else:
        print("Fehler bei der Anfrage:", response.text)

# Beispielbenutzung
while True:
    user_input = input("Du: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    send_message(user_input)
