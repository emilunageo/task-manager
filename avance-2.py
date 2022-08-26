""" 
Mi proyecto es un task manager, este programa le permitira al usuario
agregar tareas, determinar su estado y eliminarlas.

"""


""" 

------AVANCE 2

A falta de información para el avance 2 he 
decidido realizar operaciones de diferentes tipos 
con distintos problemas.

Traté de usar distintos operadores en distintos escenarios.

"""

# Calcular la fuerza de un objeto

""" def fuerza(m, a) :
    return m * a
input_m = float(input("Inserte la masa del objeto: "))
input_a = float(input("Inserte la aceleración del objeto: "))
print(f"La fuerza del objeto es: {fuerza(input_m, input_a)}N") """

# Calcular la energía requerida para subir un escalon de cierta altura.

g = 9.81 #GRAVEDAD

print("Instrucciones: Favor de insertar los valores numericos \n1. Inserte su peso en kg\n2. Inserte la altura del escalon en cm\n---------------")
def escalones(peso, altura):
    return peso * g * (altura / 100)

input_peso = float(input("Su peso: "))
input_altura = float(input("Altura escalon: "))

print(f"La energía que emplea para subir un escalon de {input_altura}cm es de {escalones(input_peso, input_altura)}J")

# Calcular los escalones que deberías subir para usar la energía de la comida chatarra
""" 
Razonamineto para determinar los escalones que que deberías subir
para utilizar la energía que te proporciona el alimento que ingieras.

1. Pasar el contenido energético de kJ a Jules multiplicando los kJ por 1,000
   Ejemplo: 2,205kJ = 2,205,000J

2. De los jules que se ingieren por medio del alimento, solo el 20% es energía 
   que nuestro cuerpo utiliza por consecuente multiplicamos 2,205,000J * 0.20
   y eso nos da como resultado 441,000J (Energía que adquirimos)

3. Debemos restar de la cantidad de energía que nos aporta el alimento
   ingerido (en este caso 441,000J) la energía que utilizamos para sobrevivir en el día
   a día, que este caso establecí un estándar de 8320J para todos los usuarios.
   441,000J - 8320J = 432,680J siendo este último resultado la cantidad aproximada
   de energía que nos aporta este alimento de ejemplo.

4. Por último dividimos 432,680J / energia utilizada para subir un escalon.
   Y ese resultado sería la cantidad de escalones que necesitas subir para
   utilizar la energía del alimento ingerido, en este caso aprox 3,769 escalones.

"""
def cuantos_escalones(kj, j_escalones):
    return  int((((kj * 1000) * 0.20) - 8320) / j_escalones)
#input_food_name = input("Inserte el nombre del alimento que desea ingerir: ")
input_kj = float(input("Inserte el contenido energetico en kj: "))

print(f"{cuantos_escalones(input_kj, escalones(input_peso, input_altura))} escalones debe subir para utilizar la energía del alimento que ingirio.")



