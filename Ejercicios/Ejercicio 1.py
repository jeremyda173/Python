# Practica numero 1

print("Sean bienvenidos al sistema vacacional de Rappi, en este formulario sabras cuantos dias te tocara vacasionar... ¡¡buena suerte!!")

Nombre = input("\n Antes de emepezar necesitamos tu nombre, ¿Cómo te llamas? \n") # Para poder saber el nombre del empleado.
Clave = int(input("\n "+ Nombre + ", ahora necesitamos que nos des la clave del departamento al que perteneces: \n")) # Para poder detectar la condicion que vamos a usar con el empleado.

if Clave > 3 : #Condicion hecha por si introducen una clave no deseada
    print("Ese departamento no esta registrado, vuelve a intentarlo.")
    
if Clave == 1 :
    print("Este es el departamento numero 1 o 'Atencion al cliente'")
    print("===========================================")
    Años= int(input("¿Cuántos años lleva de trabajo? \n"))
    if Años == 1 :
        print("Te corresponden 6 dias de vacaciones")
    elif Años >= 2 and Años <= 6 :
        print("Te corresponden 14 dias de vacaciones")
    elif Años >= 7 :
        print("Te corresponden 20 dias de vacaciones")
    else:
        print("No tienes derechos vacaciones.")

if Clave == 2 :
    print("Este es el departamento numero 2 o 'Logistica'")
    print("====================================")
    Años= int(input("¿Cuántos años lleva de trabajo? \n"))
    if Años == 1 :
        print("Te corresponden 7 dias de vacaciones")
    elif Años >= 2 and Años <= 6 :
        print("Te corresponden 15 dias de vacaciones")
    elif Años >= 7 :
        print("Te corresponden 22 dias de vacaciones")
    else:
        print("No tienes derechos vacaciones.")

if Clave == 3 :
    print("Este es el departamento numero 3 o 'Gerencia'")
    print("====================================")
    Años= int(input("¿Cuántos años lleva de trabajo? \n"))
    if Años == 1 :
        print("Te corresponden 10 dias de vacaciones")
    elif Años >= 2 and Años <= 6 :
        print("Te corresponden 20 dias de vacaciones")
    elif Años >= 7 :
        print("Te corresponden 30 dias de vacaciones")
    else:
        print("No tienes derechos vacaciones.")
        

        
