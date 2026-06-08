import json
import os

FILE_NAME = r"C:\vs\To-Do-List-App\New folder\tasks.json"

print("File path:", os.path.abspath("tasks.json"))

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)

def load_tasks():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

while True:
    print("\n===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    tasks = load_tasks()

    if choice == "1":
        task = input("Enter task: ")

        tasks.append({
            "task": task,
            "completed": False
        })

        save_tasks(tasks)
        print("✅ Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. [{status}] {task['task']}")

    elif choice == "3":
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. [{status}] {task['task']}")

            num = int(input("Enter task number: "))

            if 1 <= num <= len(tasks):
                tasks[num - 1]["completed"] = True
                save_tasks(tasks)
                print("✅ Task marked as completed!")
            else:
                print("❌ Invalid task number!")

    elif choice == "4":
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. [{status}] {task['task']}")

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks(tasks)
                print("✅ Task deleted!")
            else:
                print("❌ Invalid task number!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice!")