import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 10:
        raise ValueError("Password length should be at least 10 characters to include one of each required type.")
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    if length > 4:
        all_characters = uppercase + lowercase + digits + special
        password.extend(random.choice(all_characters) for _ in range(length - 4))

    random.shuffle(password)

    return ''.join(password)

def generate_password_gui():
    try:
        length = int(entry.get())
        if length < 10:
            messagebox.showerror("Invalid Input", "Password length should be at least 10.")
            return
        password = generate_password(length)
        result_label.config(text=f"Generated password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter the desired length of the password (at least 10):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
