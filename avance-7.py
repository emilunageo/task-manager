tasks = []
# Create task and status
def create_task():
    while True:
        input_task = input("Write the task: ")
        input_status = input("Write a status: ")
        tasks.append([input_task, input_status])
        if input_task == "exit":
            tasks.remove(["exit", "exit"])
            break

#Show tasks
def show_tasks(tasks):
    if tasks != []:
        count = 0
        print("This are your tasks: \n")
        for task in tasks:
            count += 1
            print(f"{count}. {task} \n")
    else:
        print("---- You didn't add any task yet or you already delate all your tasks, please add some to the program ----")
create_task()
show_tasks(tasks)
