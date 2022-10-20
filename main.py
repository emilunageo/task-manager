print("""Welcome to task manager pro (for pros)""")
print("""Select the option you want to run \n
1. Add taks
2. Show tasks
3. Delate tasks
4. Edit tasks
5. Exit\n""")
opcion = int(input(("Write the option: ")))
# A print menu function
def printMenu():
    print("""----------------------------------
\nSelect the option you want to run \n
1. Add taks
2. Show tasks
3. Delate tasks
4. Edit tasks
5. Exit\n
----------------------------------""")
    opcion = int(input(("Write the option: ")))
    return opcion
tasks = []
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
    if tasks != []:
        count = 0
        print("This are your tasks: \n")
        for task in tasks:
            count += 1
            print(f"{count}. {task}")
        print("")
    else:
        print("---- You didn't add any task yet or you already delate all your tasks, please add some to the program ----")
# Delate tasks
def delate_tasks():
    if tasks != []:
        print("To delate a task write the number of the task.")
        print("If you want to stop delating tasks write: exit")
        show_tasks(tasks)
        while True:
            input_task = input("Write the number of task that you want to remove: ")
            if input_task != "exit":
                input_task = int(input_task)
                if input_task > len(tasks) or input_task <= 0:
                    print("The number of task you write is not valid please try again")
                else:
                    task_want_to_remove = tasks[input_task - 1]
                    print(f"Are you sure you want to delate this task: {task_want_to_remove}")
                    decision = input("to conitune write yes or no (y/n): ")
                    if decision == "y":
                        tasks.remove(task_want_to_remove)
                        show_tasks(tasks)
                        if tasks != []:
                            continue
                        else:
                            print("\n---- You already delate every single task in the program, please add new tasks to the program ----\n")
                            break
                    else:
                        print("ok")
                        break
            else:
                print("ok")
                break
    else:
        show_tasks(tasks)
# Edit task
def edit_tasks():
    if tasks != []:
        print("To edit a task write the number of the task. Then edit the task.")
        print("If you want to stop delating tasks write: exit")
        show_tasks(tasks)
        while True:
            input_task = input("Write the number of task that you want to edit: ")
            if input_task != "exit":
                input_task = int(input_task)
                if input_task > len(tasks) or input_task <= 0:
                    print("The number of task you write is not valid please try again")
                else:
                    task_want_to_edit = tasks[input_task - 1]
                    print(f"Are you shure you want to edit this task: {task_want_to_edit}")
                    decision = input("to conitune write yes or no (y/n): ")
                    if decision == "y":
                        task_edited = input("Edit: ")
                        tasks[input_task - 1] = task_edited
                        show_tasks(tasks)
                    else:
                        print("ok")
                        break
            else:
                print("ok")
                break
    else:
        show_tasks(tasks)
         
# A while loop that allow to get back to the main menu
while opcion != 5:
    if opcion == 1:
        add_tasks()
    if opcion == 2:
        show_tasks(tasks)
    if opcion == 3:
        delate_tasks()
    if opcion == 4:
        edit_tasks()
    opcion = printMenu()