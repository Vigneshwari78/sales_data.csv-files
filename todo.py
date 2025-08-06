tasks=[]

def add_task():
    task=input("enter the task:")
    tasks.append(task)
    print(f"Task '{task}' added Successfully!")

def remove_task():
    view_tasks()
    try:
        task_num=int(input("enter the task number to remove:"))
        removed_task=tasks.pop(task_num-1)
        print(f"Task' {removed_task}' removed Successfully!")
    except(IndexError,ValueError):
        print("Invalid task number.")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nHere's you To-Do list:")
        for i,task in enumerate(tasks,start=1):
            print(i,task)

def main():
    while True:
        print("\nOptions: 1. Add Task  2. Remove Task  3. View Task  4. Exit")
        choice=input("enter your choice: ")

        if choice == '1':
           add_task()
        elif choice == '2':
           remove_task()
        elif choice == '3':
           view_tasks()
        elif choice == '4':
           print("Exiting To-Do list")
        else:
           print("Invalid choice,Try again!")

main()
