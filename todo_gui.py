# todo_gui.py

import tkinter as tk
from tkinter import messagebox

def add_task(tasks, title, description):
    if title:
        tasks.append({"title": title, "description": description, "completed": False})
        return True
    else:
        messagebox.showwarning("Input Error", "Task title is required.")
        return False

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def update_tasks(tasks, task_frame):
    for widget in task_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        task_str = f"[{status}] {task['title']}: {task['description']}"
        task_label = tk.Label(task_frame, text=task_str)
        task_label.pack(anchor="w")

        complete_button = tk.Button(task_frame, text="Complete", command=lambda i=i: complete_task(tasks, i))
        complete_button.pack(anchor="e")
        remove_button = tk.Button(task_frame, text="Remove", command=lambda i=i: remove_task(tasks, i))
        remove_button.pack(anchor="e")

def main():
    tasks = []
    app = tk.Tk()
    app.title("To-Do List")
    app.geometry("400x400")

    task_frame = tk.Frame(app)
    task_frame.pack(pady=10)

    entry_title = tk.Entry(app, width=40)
    entry_title.pack(pady=5)
    entry_description = tk.Entry(app, width=40)
    entry_description.pack(pady=5)

    add_button = tk.Button(app, text="Add Task", command=lambda: add_task(tasks, entry_title.get(), entry_description.get()))
    add_button.pack(pady=5)

    update_tasks(tasks, task_frame)

    app.mainloop()

if __name__ == "__main__":
    main()
