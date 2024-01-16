# Haciendo sentencias condicionales simples y compuestas

"Realizando el promedio de 3 notas para saber si aprobe o no el curso"

print("Welcome")

Nombre = input("Para empezar, ¿Cuál es nombre? ")

Matematica = int(input(Nombre + " ¿Cuál es tu nota en Matemáticas? "))
Ciencias = int(input(Nombre + "¿Cuál es tu nota en Ciencias? "))
English = int(input(Nombre + "¿Cuál es tu nota en English? "))

Total = (Matematica + Ciencias + English) / 3
 Total = int(Total)# para solo tomar el valor entero

if Total >= 6 :
     print("Felicidades " + Nombre + ", pasaste de grado con un promedio de: ",round(Total,1), "Genial!!") #para que tome un valor despues del punto
else :
     print("Malas noticias, tu promedio quedo en: ",round(Total,1), "lo cual no es suficiente para avanzar. ""Buena suerte")