'''Calcular la edad de una persona y determinar si es mayor o menor de edad (Algoritmo del tipo cuantitativo).'''
print("Hola, este algoritmo trata sobre determinar la edad\n")

Año_nacimiento = int(input("Introduce el año de nacimiento: "))
Año_actual = int(input("Introduce año actual: "))
Edad = (Año_actual - Año_nacimiento)

if Edad >= 18:
    print("Tienes", Edad, "años de edad.", "Asi que, eres mayor de edad")
else:
    print("Tienes", Edad, "años de edad.", "Asi que, eres menor de edad")

    