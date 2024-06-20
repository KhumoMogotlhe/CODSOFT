import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_round(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    if result == 'tie':
        result_text = f"Both chose {user_choice}. It's a tie!"
    elif result == 'user':
        result_text = f"You chose {user_choice} and the computer chose {computer_choice}. You win!"
    else:
        result_text = f"You chose {user_choice} and the computer chose {computer_choice}. You lose!"
    
    messagebox.showinfo("Result", result_text)
    
    update_scores(result)

def update_scores(result):
    global user_score, computer_score
    if result == 'user':
        user_score += 1
    elif result == 'computer':
        computer_score += 1
    
    score_label.config(text=f"Scores - You: {user_score}, Computer: {computer_score}")

def on_click(choice):
    play_round(choice)

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.configure(bg='pink')


score_label = tk.Label(root, text=f"Scores - You: {user_score}, Computer: {computer_score}", font=('Helvetica', 16))
score_label.pack(pady=20)

rock_button = tk.Button(root, text="Rock", width=15, height=2, command=lambda: on_click('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, height=2, command=lambda: on_click('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, height=2, command=lambda: on_click('scissors'))
scissors_button.pack(pady=5)

# Run the main event loop
root.mainloop()
