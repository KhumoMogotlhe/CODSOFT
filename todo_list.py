# todo_cli.py

def add_task(tasks, title, description=""):
    tasks.append({"title": title, "description": description, "completed": False})

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        return "Invalid task number."

def update_task(tasks, index, title=None, description=None):
    if 0 <= index < len(tasks):
        if title:
            tasks[index]["title"] = title
        if description:
            tasks[index]["description"] = description
    else:
        return "Invalid task number."

def mark_task_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        return "Invalid task number."

def list_tasks(tasks):
    result = []
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        result.append(f"{i + 1}. [{status}] {task['title']}: {task['description']}")
    return result

def main():
    tasks = []
    
    while True:
        print("\nTo-Do List:")
        for task in list_tasks(tasks):
            print(task)
        print("\nCommands: add, remove, update, complete, exit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(tasks, title, description)
        elif command == "remove":
            index = int(input("Enter task number to remove: ")) - 1
            print(remove_task(tasks, index) or "")
        elif command == "update":
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new task title (or press Enter to skip): ")
            description = input("Enter new task description (or press Enter to skip): ")
            print(update_task(tasks, index, title or None, description or None) or "")
        elif command == "complete":
            index = int(input("Enter task number to mark as complete: ")) - 1
            print(mark_task_complete(tasks, index) or "")
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
