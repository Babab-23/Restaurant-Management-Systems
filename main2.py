import tkinter as tk
import random
from tkinter import messagebox

# Function to determine the winner
def play(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n\n{result}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24, "bold"))
heading.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Rock button
rock_button = tk.Button(button_frame, text="Rock", width=15, height=2, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

# Paper button
paper_button = tk.Button(button_frame, text="Paper", width=15, height=2, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

# Scissors button
scissors_button = tk.Button(button_frame, text="Scissors", width=15, height=2, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Exit button
exit_button = tk.Button(root, text="Exit", width=10, command=root.destroy)
exit_button.pack(pady=20)

# Start the application
root.mainloop()
