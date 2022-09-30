"""
1. Crear un menú con la opción que el usuario desea ejecutar.
(a. Ingresar tareas y estado de tarea, b. Cambiar el estado de las tareas, 
c. Ver tareas y estados, d. Eliminar tareas )

A) Mientras que el usuario haya elegido la opción de añadir tareas, añadir tareas con su estado valor
predeterminado 0 (por hacer) hasta que se cumpla una condición en específico en el ciclo.

B) Si hay tareas entonces pedir al usuario que escriba el numero de la tarea que desea cambiar el estado.
Si no hay tareas perdirle al usuairio que añada tareas y volver al menú inicial.

C) Si hay tareas entonces mostrar tareas y su estado. Si no hay tareas pedir al usuario que añada tareas.

D) Si hay tareas entonces pedir al usuario que escriba el numero de la tarea que desea eliminar
y verificar si desea continuar con un y/n. Si no hay tareas pedirle al usuario que añada tareas.



"""

""" for x in range(number_of_tasks):
    task = input(f"{x+1}. Escribe la tarea que deseas añadir: ")
    add_tasks(task) """

from atexit import register


tasks = []
counter = 0
def add_tasks(task):
    tasks.append(task)
# Mostrar tareas
def show_tasks(tasks):
    for task in tasks:
        print(f"\n{counter}. {task} \n")

#Inicio del programa
print("""Te doy la bienevenida al administrador de tareas.. \n
A continuación ingresa el número de la opción que deseas ejetucar, siendo estás: \n
1. Añadir Tareas\n
2. Ver tareas\n
3. Eliminar tareas\n
4. Salir del programa\n""")

option = int(input("Ingresa el número de la acción que deseas ejecutar: "))
if option == 1:
    print("""Para añadir tareas ingrese tantas tareas como desee y cuando quiera parar escriba: exit""")
    while True:
        task = input(f"Escribe la tarea que deseas añadir: ")
        add_tasks(task)
        if task == "exit":
            show = input("Deseas ver las tareas que añadiste? y/n:  ")
            if show == "n":
                print("OK")
            if show == "y":
                tasks.remove("exit")
                print("Estás son las tareas que has añadido al programa:")
                show_tasks(tasks)
            break
if option == 2:
    print("Estás son las tareas que has añadido: ")
if option == 3:
    print("Se eliminaron las tareas")
if option == 4:
    print("Bye :)")

