# Start of the program
from http.client import OK


print("""Select the option you want to run \n
1. Add taks\n
2. Show tasks\n
3. Delate tasks\n
4. Exit\n""")
opcion = int(input(("Write the option: ")))

# A print menu function
def printMenu():
    print("""Select the option you want to run \n
    1. Add taks\n
    2. Show tasks\n
    3. Delate tasks\n
    4. Exit\n""")
    opcion = int(input(("Write the option: ")))
    return opcion

tasks = []
delating_list = []
# Create tasks:
def add_tasks():
    print("If you want to stop adding tasks write: exit")
    while True:
        input_task = input("Write the task: ")
        tasks.append(input_task)
        if input_task == "exit":
            tasks.remove("exit")
            break
# Show tasks
def show_tasks(tasks):
    count = 0
    print("This are your tasks: ")
    for task in tasks:
        count += 1
        print(f"\n{count}. {task}\n")

# Delate tasks
def delate_tasks():
    print("To delate a task write the the number the task.")
    print("If you want to stop delating tasks write: exit")
    while True:
        show_tasks(tasks)
        input_task = input("Write the number of task that you want to remove: ")
        if input_task != "exit":
            input_task = int(input_task)
            if input_task > len(tasks) + 1 or input_task <= 0:
                print("The number of task you write is not valid please try again")
            else:
                task_want_to_remove = tasks.index(input_task)
                print(f"Are you sure you want to delate this task: {task_want_to_remove} \n")
                decision = input("y/n to conitune: ")
                if decision == "y":
                    tasks.remove(task_want_to_remove)
                    show_tasks(tasks)
                else:
                    print("ok")
                    break
        else:
            print("ok")
            break
# A while loop that allow to get back to the main menu
while opcion != 4:
    if opcion == 1:
        add_tasks()
    if opcion == 2:
        show_tasks(tasks)
    if opcion == 3:
        delate_tasks()
    opcion = printMenu()

