import json


tasks = []


def load_tasks():
    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        print("Error reading tasks file. Starting with an empty list.")
        tasks = []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = input("Enter your task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "task": task,
        "done": False
    })

    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['task']} - {status}")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number!")
            return

        deleted_task = tasks.pop(number - 1)
        save_tasks()
        print(f"Deleted: {deleted_task['task']}")

    except ValueError:
        print("Please enter a valid number!")


def mark_task_done():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark as done: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number!")
            return

        tasks[number - 1]["done"] = True
        save_tasks()
        print("Task marked as done!")

    except ValueError:
        print("Please enter a valid number!")


load_tasks()

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        mark_task_done()

    elif choice == "5":
        print("To-Do List Manager is closing...")
        break

    else:
        print("Invalid choice!")