tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")