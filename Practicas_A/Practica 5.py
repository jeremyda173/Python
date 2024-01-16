''' Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde. '''

Nombre = input("¿Cómo te llamas? ")
Horas = int(input(f"Hola {Nombre}, ¿Cuantas horas trabajas? " ))
Ganancia = int(input("Y, ¿Cuanto pagan por hora de trabajo? "))

if Horas >= 1 :
     print(Ganancia * Horas, "dolares la hora")
else:
    print("Ganancia = Tiene que hablar con el gerente.")