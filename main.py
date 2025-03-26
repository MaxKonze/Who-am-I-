import tkinter as tk

# Die Klasse, die das Spiel implementiert
class WhoAmIGame:
    def __init__(self, root):
        # Initialisiert das Hauptfenster (root)
        self.root = root
        self.root.title("Who Am I Game")  # Setzt den Titel des Fensters
        self.root.attributes("-fullscreen", True)  # Setzt das Fenster auf Vollbild

        # Variablen, um den Spielfortschritt zu speichern
        self.tries = 0  # Zählt die Versuche
        self.player_name = ""  # Speichert den Namen des Spielers
        self.mode = ""  # Speichert den Modus des Spiels (ob AI oder Player rät)

        # Erstellen eines Frames, um die Widgets zu gruppieren
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)  # Packt den Frame und sorgt dafür, dass er sich ausdehnt

        # Begrüßungstext
        self.greeting = tk.Label(self.frame, text="Welcome to our Who Am I game", font=("Arial", 32, "bold"))
        self.greeting.pack(pady=20)  # Fügt den Begrüßungstext hinzu

        # Start-Button, um das Spiel zu beginnen
        self.start_button = tk.Button(self.frame, text="Start", font=("Arial", 24, "bold"), command=self.start_game)
        self.start_button.pack(pady=20)  # Packt den Start-Button

        # Binden der Escape-Taste, um das Fenster zu schließen
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    # Funktion, um das Spiel zu starten
    def start_game(self):
        self.greeting.config(text="Select Mode")  # Begrüßungstext ändern
        self.start_button.pack_forget()  # Versteckt den Start-Button

        # Label zur Auswahl des Modus
        self.mode_label = tk.Label(self.frame, text="Who will guess?", font=("Arial", 24))
        self.mode_label.pack(pady=10)

        # Frame für die Modus-Auswahl-Buttons
        self.mode_buttons = tk.Frame(self.frame)
        self.mode_buttons.pack(pady=10)

        # Zwei Buttons zur Auswahl, ob der Spieler oder die AI rät
        self.ai_button = tk.Button(self.mode_buttons, text="AI guesses", font=("Arial", 20),
                                   command=lambda: self.select_mode("AI"))
        self.player_button = tk.Button(self.mode_buttons, text="Player guesses", font=("Arial", 20),
                                       command=lambda: self.select_mode("Player"))
        self.ai_button.pack(side=tk.LEFT, padx=10)
        self.player_button.pack(side=tk.LEFT, padx=10)

    # Funktion, um den Modus auszuwählen
    def select_mode(self, selected_mode):
        self.mode = selected_mode  # Setzt den Modus auf die Auswahl
        self.tries = 0
        self.mode_label.pack_forget()  # Versteckt das Modus-Label
        self.mode_buttons.pack_forget()  # Versteckt die Modus-Buttons

        # Wenn der Modus "AI" ist, frage nach dem Namen
        if self.mode == "AI":
            self.ask_for_name()
        else:
            self.show_player_guess_screen()  # Zeige den Bildschirm für den Spieler-Rate-Modus

    # Funktion, um nach dem Namen zu fragen
    def ask_for_name(self):
        self.name_label = tk.Label(self.frame, text="Enter the name of the person that you are thinking of:", font=("Arial", 20))
        self.name_label.pack(pady=10)

        # Eingabefeld für den Namen
        self.name_entry = tk.Entry(self.frame, font=("Arial", 20))
        self.name_entry.pack(pady=10)
        self.name_entry.bind("<KeyRelease>", self.on_entry_change)  # Binde das Ereignis des Tasten-Loslassens

        # Submit-Button für den Namen, der standardmäßig deaktiviert ist
        self.submit_button = tk.Button(self.frame, text="Submit", font=("Arial", 20), state=tk.DISABLED,
                                       command=self.save_name)
        self.submit_button.pack(pady=10)

    # Funktion, die bei jeder Änderung im Eingabefeld ausgeführt wird
    def on_entry_change(self, event):
        if self.name_entry.get().strip():  # Überprüft, ob der Text nicht leer ist
            self.submit_button.config(state=tk.NORMAL)  # Aktiviert den Submit-Button
        else:
            self.submit_button.config(state=tk.DISABLED)  # Deaktiviert den Submit-Button

    # Funktion, um den Namen zu speichern und das Spiel zu starten
    def save_name(self):
        self.player_name = self.name_entry.get().strip()  # Speichert den Namen des Spielers
        if self.player_name:  # Wenn der Name nicht leer ist
            self.show_game_screen()  # Zeige den Spielfortschritt

    # Funktion, um den Spielbildschirm anzuzeigen
    def show_game_screen(self):
        self.clear_frame()  # Löscht alle vorherigen Widgets

        # Anzeige des Spieler-Namens
        tk.Label(self.root, text=f"Player: {self.player_name}", font=("Arial", 16), anchor="w").place(x=10,
                                                                                                      y=self.root.winfo_screenheight() - 40)

        # Frage, die der Spieler beantworten muss
        self.question_label = tk.Label(self.frame, text="[API-Text kommt hier]", font=("Arial", 24, "bold"))
        self.question_label.pack(pady=20)

        # Frame für die Buttons zur Beantwortung der Frage
        button_frame = tk.Frame(self.frame)
        button_frame.pack()

        # Buttons für "Ja", "Nein", "Ich weiß nicht" und "Richtige Antwort"
        self.yes_button = tk.Button(button_frame, text="Yes", font=("Arial", 20), command=self.increment_tries)
        self.yes_button.pack(side=tk.LEFT, padx=20)

        self.no_button = tk.Button(button_frame, text="No", font=("Arial", 20), command=self.increment_tries)
        self.no_button.pack(side=tk.LEFT, padx=20)

        self.idk_button = tk.Button(button_frame, text="I Don't Know", font=("Arial", 20), command=self.increment_tries)
        self.idk_button.pack(side=tk.LEFT, padx=20)

        self.right_guess_button = tk.Button(button_frame, text="Right Guess", font=("Arial", 20),
                                            command=self.show_result)
        self.right_guess_button.pack(side=tk.LEFT, padx=20)

    # Funktion, um den Bildschirm für den Spieler-Rate-Modus anzuzeigen
    def show_player_guess_screen(self):
        self.clear_frame()  # Löscht vorherige Widgets

        # Label für den Spieler, um zu erraten, was die AI denkt
        tk.Label(self.frame, text="Guess what the AI is thinking!", font=("Arial", 24, "bold")).pack(pady=20)

        # Eingabefeld für den Rateversuch des Spielers
        self.player_input = tk.Entry(self.frame, font=("Arial", 20))
        self.player_input.pack(pady=10)
        self.player_input.bind("<KeyRelease>", self.on_player_entry_change)  # Bindet die Änderung des Eingabefelds

        # Submit-Button für den Rateversuch, der standardmäßig deaktiviert ist
        self.submit_guess_button = tk.Button(self.frame, text="Submit Guess", font=("Arial", 20), state=tk.DISABLED,
                                             command=self.increment_tries_player)
        self.submit_guess_button.pack(pady=10)

        # Button für "Richtige Antwort"
        self.guess_correct_button = tk.Button(self.frame, text="Guessed it Correct", font=("Arial", 20),
                                              command=self.show_player_result)
        self.guess_correct_button.pack(pady=10)

    # Funktion, die bei jeder Änderung im Rate-Eingabefeld ausgeführt wird
    def on_player_entry_change(self, event):
        if self.player_input.get().strip():  # Überprüft, ob der Text im Rate-Eingabefeld nicht leer ist
            self.submit_guess_button.config(state=tk.NORMAL)  # Aktiviert den Submit-Button
        else:
            self.submit_guess_button.config(state=tk.DISABLED)  # Deaktiviert den Submit-Button

    # Funktion, um die Versuche zu erhöhen
    def increment_tries(self):
        self.tries += 1

    # Funktion, um die Versuche zu erhöhen und das Eingabefeld zu leeren (bei Rateversuchen)
    def increment_tries_player(self):
        self.tries += 1
        self.player_input.delete(0, tk.END)  # Löscht das Eingabefeld nach dem Versuch

    # Funktion, um das Ergebnis anzuzeigen, wenn der Spieler erraten wurde
    def show_result(self):
        self.clear_frame()  # Löscht vorherige Widgets
        tk.Label(self.frame, text=f"{self.player_name} was guessed in {self.tries} tries!",
                 font=("Arial", 24, "bold")).pack(pady=20)
        tk.Button(self.frame, text="Exit", font=("Arial", 20), command=self.root.destroy).pack(pady=20)

    # Funktion, um das Ergebnis anzuzeigen, wenn der Spieler die richtige Antwort erraten hat
    def show_player_result(self):
        self.clear_frame()  # Löscht vorherige Widgets
        tk.Label(self.frame, text=f"You guessed it in {self.tries} tries!", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Button(self.frame, text="Exit", font=("Arial", 20), command=self.root.destroy).pack(pady=20)

    # Funktion, um alle Widgets im Frame zu löschen
    def clear_frame(self):
        for widget in self.frame.winfo_children():  # Durchläuft alle Widgets im Frame
            widget.destroy()  # Löscht jedes Widget

# Hauptteil des Programms
if __name__ == "__main__":
    root = tk.Tk()  # Erstellen des Hauptfensters
    game = WhoAmIGame(root)  # Erstellen des Spiels
    root.mainloop()  # Startet die Tkinter-Event-Schleife
