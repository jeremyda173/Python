# El metodo format() para la concatenacion 
# Ademas con este metodo puedo ordenar las variables poniendo los lugares en que se encuentra esta 

Nombre = input("Escribe tu nombre: ")
Edad = int(input("Escribe tu edad: "))

Resultado = "Hola {}, tienes {} años de edad.".format(Nombre, Edad)
print(Resultado)

#El metodo f-strings

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

print(f"Hola {nombre} tienes {edad} años")

nombre1 = input("Escribe tu nombre: ")
num_1 = int(input("Escribe un numero: "))
num_2 = int(input("Escribe un numero: "))

print(f"Hola {nombre1} el resultado de {num_1 } + {num_2} es: {num_1 + num_2}")