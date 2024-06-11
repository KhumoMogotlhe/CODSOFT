import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x500")

        self.result_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Configure the main window background color
        self.configure(bg="#ffe6f2")
        
        # Entry field for displaying results
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ffccf2", fg="#000000")
        entry.grid(row=0, column=0, columnspan=4)

        # Define button colors
        button_bg = "#ffb3d9"
        operator_bg = "#ff66b3"
        clear_bg = "#ff3399"
        delete_bg = "#ff99cc"
        equal_bg = "#ff6699"
        
        # Create buttons
        buttons = [
            ('7', button_bg), ('8', button_bg), ('9', button_bg), ('/', operator_bg),
            ('4', button_bg), ('5', button_bg), ('6', button_bg), ('*', operator_bg),
            ('1', button_bg), ('2', button_bg), ('3', button_bg), ('-', operator_bg),
            ('0', button_bg), ('.', button_bg), ('=', equal_bg), ('+', operator_bg)
        ]

        row_val = 1
        col_val = 0

        for (button_text, color) in buttons:
            button = tk.Button(self, text=button_text, font=("Arial", 18), bd=5, padx=10, pady=10, bg=color, command=lambda x=button_text: self.on_button_click(x))
            button.grid(row=row_val, column=col_val, sticky="nsew")

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Add Clear and Delete buttons
        clear_button = tk.Button(self, text='C', font=("Arial", 18), bd=5, padx=10, pady=10, bg=clear_bg, command=self.clear)
        clear_button.grid(row=row_val, column=0, sticky="nsew")

        delete_button = tk.Button(self, text='DEL', font=("Arial", 18), bd=5, padx=10, pady=10, bg=delete_bg, command=self.delete)
        delete_button.grid(row=row_val, column=1, sticky="nsew")

        # Configure grid
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char == "=":
            try:
                # Evaluate the expression
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Append the clicked button's text to the entry field
            self.result_var.set(current_text + char)
    
    def clear(self):
        self.result_var.set("")
    
    def delete(self):
        current_text = self.result_var.get()
        self.result_var.set(current_text[:-1])

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
