# Continuando con cadenas de caracteres

Nombre = "Jeremy" #declaracion de una variable
Nombre += " " #usando el operador de asignacion (+ y =) puedo agregar caracteres a nuestra variable inicial
Nombre += "Domínguez"

print(Nombre) #resultado del proceso

#Operador de concatenacion

Nombre = "Jeremy"
espacio = " "
Apellido_1 = "Dominguez"
Apellido_2 = "Angeles"
print(Nombre + espacio + Apellido_1 + espacio +Apellido_2)

numero_1 = 7
numero_2 = 29
resultado = numero_1 + numero_2
resultado = str(resultado) #para convertir un valor tipo numero a tipo texto osea, de un numero entero a un string
print("El resultado de la suma es: " + resultado)
