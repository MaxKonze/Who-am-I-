import tkinter as tk


# The class that implements the game
class WhoAmIGame:
    def __init__(self, root):
        # Initialize the main window (root)
        self.root = root
        self.root.title("Who Am I Game")  # Set window title
        self.root.attributes("-fullscreen", True)  # Set fullscreen window

        # Variables to track game progress
        self.tries = 0  # Counts the number of tries
        self.player_name = ""  # Stores the player's name
        self.mode = ""  # Stores the mode of the game (whether AI or Player guesses)
        self.last_button_pressed = None  # Stores which button (Yes/No/IDK) was last pressed

        # Create a frame to group widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)  # Ensure the frame expands

        # Welcome text
        self.greeting = tk.Label(self.frame, text="Welcome to our Who Am I game", font=("Arial", 32, "bold"))
        self.greeting.pack(pady=20)  # Add the welcome text

        # Start button to begin the game
        self.start_button = tk.Button(self.frame, text="Start", font=("Arial", 24, "bold"), command=self.start_game)
        self.start_button.pack(pady=20)  # Pack the start button

        # Bind the Escape key to close the window
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    # Function to start the game
    def start_game(self):
        self.greeting.config(text="Select Mode")  # Update welcome text
        self.start_button.pack_forget()  # Hide the start button

        # Label for mode selection
        self.mode_label = tk.Label(self.frame, text="Who will guess?", font=("Arial", 24))
        self.mode_label.pack(pady=10)

        # Frame for mode selection buttons
        self.mode_buttons = tk.Frame(self.frame)
        self.mode_buttons.pack(pady=10)

        # Buttons for selecting whether AI or Player guesses
        self.ai_button = tk.Button(self.mode_buttons, text="AI guesses", font=("Arial", 20),
                                   command=lambda: self.select_mode("AI"))
        self.player_button = tk.Button(self.mode_buttons, text="Player guesses", font=("Arial", 20),
                                       command=lambda: self.select_mode("Player"))
        self.ai_button.pack(side=tk.LEFT, padx=10)
        self.player_button.pack(side=tk.LEFT, padx=10)

    # Function to select mode
    def select_mode(self, selected_mode):
        self.mode = selected_mode  # Set the mode to the selected option
        self.tries = 0
        self.mode_label.pack_forget()  # Hide the mode label
        self.mode_buttons.pack_forget()  # Hide the mode selection buttons

        # If the mode is "AI", ask for the name
        if self.mode == "AI":
            self.ask_for_name()
        else:
            self.show_player_guess_screen()  # Show the screen for Player Guess mode

    # Function to ask for the player's name
    def ask_for_name(self):
        self.name_label = tk.Label(self.frame, text="Enter the name of the person that you are thinking of:",
                                   font=("Arial", 20))
        self.name_label.pack(pady=10)

        # Input field for the player's name
        self.name_entry = tk.Entry(self.frame, font=("Arial", 20))
        self.name_entry.pack(pady=10)
        self.name_entry.bind("<KeyRelease>", self.on_entry_change)  # Bind the key release event

        # Submit button for the player's name, initially disabled
        self.submit_button = tk.Button(self.frame, text="Submit", font=("Arial", 20), state=tk.DISABLED,
                                       command=self.save_name)
        self.submit_button.pack(pady=10)

    # Function to handle text input in the name field
    def on_entry_change(self, event):
        # Enable the submit button if the name field is not empty
        if self.name_entry.get().strip():
            self.submit_button.config(state=tk.NORMAL)
        else:
            self.submit_button.config(state=tk.DISABLED)

    # Function to save the player's name and start the game
    def save_name(self):
        self.player_name = self.name_entry.get().strip()  # Store the player's name
        if self.player_name:  # If the name is not empty
            self.show_game_screen()  # Show the game screen

    # Function to show the game screen
    def show_game_screen(self):
        self.clear_frame()  # Clear all previous widgets

        # Display the player's name
        tk.Label(self.root, text=f"Player: {self.player_name}", font=("Arial", 16), anchor="w").place(
            x=10, y=self.root.winfo_screenheight() - 40)

        # Display the question
        self.question_label = tk.Label(self.frame, text="[API-Text comes here]", font=("Arial", 24, "bold"))
        self.question_label.pack(pady=20)

        # Frame for answer buttons
        button_frame = tk.Frame(self.frame)
        button_frame.pack()

        # Buttons for "Yes", "No", "IDK"
        self.yes_button = tk.Button(button_frame, text="Yes", font=("Arial", 20),
                                    command=lambda: self.handle_button_press("Yes"))
        self.yes_button.pack(side=tk.LEFT, padx=20)

        self.no_button = tk.Button(button_frame, text="No", font=("Arial", 20),
                                   command=lambda: self.handle_button_press("No"))
        self.no_button.pack(side=tk.LEFT, padx=20)

        self.idk_button = tk.Button(button_frame, text="I Don't Know", font=("Arial", 20),
                                    command=lambda: self.handle_button_press("IDK"))
        self.idk_button.pack(side=tk.LEFT, padx=20)

        # Button for the "Right Guess"
        self.right_guess_button = tk.Button(button_frame, text="Right Guess", font=("Arial", 20),
                                            command=self.show_result)
        self.right_guess_button.pack(side=tk.LEFT, padx=20)

    # Function to log and save which button was pressed
    def handle_button_press(self, button_value):
        self.last_button_pressed = button_value  # Save the button that was last pressed
        self.increment_tries()  # Increment the number of tries
        print(f"'{button_value}' button was pressed.")  # Test

    # Function to increase the number of tries
    def increment_tries(self):
        self.tries += 1

    # Function to show the result if the AI guesses correctly
    def show_result(self):
        self.clear_frame()  # Clear previous widgets
        tk.Label(self.frame, text=f"{self.player_name} was guessed in {self.tries} tries!",
                 font=("Arial", 24, "bold")).pack(pady=20)
        tk.Button(self.frame, text="Exit", font=("Arial", 20), command=self.root.destroy).pack(pady=20)

    # Function to show the player guess screen
    def show_player_guess_screen(self):
        self.clear_frame()  # Clear previous widgets

        tk.Label(self.frame, text="Guess what the AI is thinking!", font=("Arial", 24, "bold")).pack(pady=20)

        # Player's input for guesses
        self.player_input = tk.Entry(self.frame, font=("Arial", 20))
        self.player_input.pack(pady=10)
        self.player_input.bind("<KeyRelease>", self.on_player_entry_change)

        # Submit guess button (initially disabled)
        self.submit_guess_button = tk.Button(self.frame, text="Submit Guess", font=("Arial", 20), state=tk.DISABLED,
                                             command=self.question_handle)
        self.submit_guess_button.pack(pady=10)

        # Button for "Guessed it Correct"
        self.guess_correct_button = tk.Button(self.frame, text="Guessed it Correct", font=("Arial", 20),
                                              command=self.show_result)
        self.guess_correct_button.pack(pady=10)

        # Funktion zum Verarbeiten des Spieler-Inputs
    def question_handle(self):
        self.question = self.player_input.get()  # Speichert die eingegebene Frage
        self.increment_tries()
        print(self.question) # Test


    # Function to enable/disable the submit guess button
    def on_player_entry_change(self, event):
        if self.player_input.get().strip():
            self.submit_guess_button.config(state=tk.NORMAL)
        else:
            self.submit_guess_button.config(state=tk.DISABLED)

    # Function to clear the frame (remove all widgets)
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


# Main part of the program
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    game = WhoAmIGame(root)  # Create the game instance
    root.mainloop()  # Start the Tkinter event loop
