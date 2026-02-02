def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")


def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")


def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Error deleting task.")


while True:
    print("\nTo-Do List Menu")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
