#Full CLI Project - Task Manager

tasks = []

def show_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: "))
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number")
    except:
        print("Invalid input")

# main loop
while True:

    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

'''
output:-

===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Delete Task
4. Exit

Enter choice: 1
Enter task: Learn Python
Task added successfully

Enter choice: 2

Your Tasks:
1. Learn Python

Enter choice: 3
Enter task number to delete: 1
Deleted task: Learn Python

Enter choice: 4
Exiting program...
'''