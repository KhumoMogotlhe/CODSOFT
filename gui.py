import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# main window
root = tk.Tk()
root.title("Simple Calculator")

# fields and labels
tk.Label(root, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# the operation buttons
operation_var = tk.StringVar()
operation_var.set('+')

operations = ['+', '-', '*', '/']
for i, operation in enumerate(operations):
    tk.Radiobutton(root, text=operation, variable=operation_var, value=operation).grid(row=2, column=i, padx=10, pady=10)

#the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=4, pady=10)

# result label
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, columnspan=4, pady=10)

# Run the Tkinter event loop
root.mainloop()
