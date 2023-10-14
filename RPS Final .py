import tkinter as tk
import random
from PIL import Image, ImageTk

def get_computer_choice():
    """
    Randomly selects a choice for the computer (rock, paper, or scissors).

    Returns:
        str: The computer's choice.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """
    Determines the winner of the game based on the player's and computer's choices.

    Args:
        player_choice (str): The player's choice (rock, paper, or scissors).
        computer_choice (str): The computer's choice (rock, paper, or scissors).

    Returns:
        str: The game result message (e.g., "You win!" or "Computer wins!").
    """
    if player_choice == computer_choice:
        return "It's a tie!"

    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "paper" and computer_choice == "rock") or \
       (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"

    return "Computer wins!"

def play():
    """
    Plays a round of Rock, Paper, Scissors, updates the result, and keeps track of scores.
    """
    player_choice = player_choice_var.get()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"Computer chooses {computer_choice}\n{result}")

    global player_score, computer_score
    if "You win!" in result:
        player_score += 1
    elif "Computer wins!" in result:
        computer_score += 1
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

def begin_game():
    """Hides the main menu and shows the game window."""
    root.withdraw()
    game_window.deiconify()

def show_rules():
    """Hides the main menu and shows the rules window."""
    root.withdraw()
    rules_window.deiconify()

def back_to_start():
    """Hides the game and rules windows and shows the main menu."""
    game_window.withdraw()
    rules_window.withdraw()
    root.deiconify()

# Initialize the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

player_choice_var = tk.StringVar()
player_score, computer_score = 0, 0

# Create and configure "Begin" button
begin_button = tk.Button(root, text="Begin", command=begin_game)
begin_button.pack()

# Create and configure "Rules" button
rules_button = tk.Button(root, text="Rules", command=show_rules)
rules_button.pack()

# Initialize the game window
game_window = tk.Toplevel()
game_window.title("Rock, Paper, Scissors Game")
game_window.withdraw()

# Load the "battle.jpg" image
battle_bg_image = Image.open("battle.jpg")
battle_bg_photo = ImageTk.PhotoImage(battle_bg_image)

# Create a Label for the background image
battle_bg_label = tk.Label(game_window, image=battle_bg_photo)
battle_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create radio buttons for player choices
choices = ["rock", "paper", "scissors"]
for choice in choices:
    radio_button = tk.Radiobutton(game_window, text=choice, variable=player_choice_var, value=choice)
    radio_button.pack()

# Create and configure "Play" button
play_button = tk.Button(game_window, text="Play", command=play)
play_button.pack()

# Create and configure "Exit" button
exit_button = tk.Button(game_window, text="Exit", command=root.destroy)
exit_button.pack()

# Create a label to display the game result
result_label = tk.Label(game_window, text="")
result_label.pack()

# Create a label to display the scores
score_label = tk.Label(game_window, text=f"Player: {player_score}  Computer: {computer_score}")
score_label.pack()

# Initialize the rules window
rules_window = tk.Toplevel()
rules_window.title("Rules")
rules_window.withdraw()

# Load the "rules.jpg" image
rules_bg_image = Image.open("rules.jpg")
rules_bg_photo = ImageTk.PhotoImage(rules_bg_image)

# Create a Label for the background image
rules_bg_label = tk.Label(rules_window, image=rules_bg_photo)
rules_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Display the rules
rules_label = tk.Label(rules_window, text="Rock, Paper, Scissors Rules:\n\n"
                                        "1. Rock beats Scissors\n"
                                        "2. Scissors beats Paper\n"
                                        "3. Paper beats Rock\n")
rules_label.pack()

# Create and configure "Back to Start" button
back_button = tk.Button(rules_window, text="Back to Start", command=back_to_start)
back_button.pack()

# Start the application main loop
root.mainloop()
