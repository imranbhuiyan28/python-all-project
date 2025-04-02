

tasks = []

def main():
    print("Welcome to To-Do List App")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Exit")
        user_input = input("Choose the option: ")

        if user_input == '6':
            print("Thank you for using our app! ")
            break
        elif user_input == '1':
            add_task()
        elif user_input == '2':
            view_task()
        elif user_input == '3':
            mark_complete()
        elif user_input == '4':
            update_task()
        elif user_input == '5':
            remove_task()
        else:
            print("Invalid option. Please try again.")


def add_task():
    task = input("Enter the task to add: ")
    tasks.append({"Task": task, "completed": False})
    print(f"{task} has been added to the tasks")


def view_task():
    if not tasks:
        print("There is no task. Please add task!")
    else:
        print("Current task.")
        for index ,  item in enumerate (tasks, 1):
            status = "✅" if item["completed"] else "⏳"
            # print(f"{index}. {item["tasks"]} - {status}")
            print(f"{index}. {item['Task']} - {status}")



def mark_complete():
    view_task()
    try:
        if not tasks:
            print("there is no task. Please add task! ")

        else:
            task_number = int(input("Enter the task number to complete the task: ")) - 1
            if task_number < len(tasks):
                tasks[task_number]["completed"] = True
                print("Your task has been completed. ")

            else:
                print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def remove_task():
    view_task()
    try:
        delete_task = int(input("Enter the task number to delete: ")) -1
        if delete_task < len(tasks):
            tasks.pop(delete_task)
            print(f"Your task  has been removed ")
        else:
            print("Invalid task number.")

    except ValueError :
        print("Please enter a valid number.")


def update_task():
    view_task()
    try:
        task_number = int(input("Enter the task number to update: ")) -1
        if  task_number < len(tasks):
            new_task = input("Enter new task to update: ")
            tasks[task_number]["Task"] = new_task
            print("Task update successful.")

        else:
            print("Please enter a valid number. ")
    except ValueError:
        print("Please enter a valid number.")




main()