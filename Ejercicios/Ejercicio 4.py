# Calculadora con una sola variable

print("Elige una opcion para empezar: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Divison")
print("5. Potencia")
print("6. Division entera")
print("7. Modulo o Resto \n")


numero = int(input("Introduce el numero de la opcion deseada: "))

if numero == 1:
    print("Elegiste la Suma \n")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado es: '", numero, "'")
elif numero == 2:
    print("Elegiste la Resta \n")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado es: '", numero, "'")
elif numero == 3:
    print("Elegiste la Multiplicacion \n")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado es: '", numero, "'")
elif numero == 4:
    print("Elegiste la Division \n")
    numero = int(input("Introduce el primer numero: "))
    numero /= int(input("Introduce el segundo numero: "))
    print("El resultado es: '", numero, "'")
elif numero == 5:
    print("Elegiste la Potencia \n")
    numero = int(input("Introduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print("El resultado es: '", numero, "'")
elif numero == 6:
    print("Elegiste la Division entera \n")
    numero = int(input("Introduce el primer numero: "))
    numero //= int(input("Introduce el segundo numero: "))
    print("El resultado es: '", numero, "'")
elif numero == 7:
    print("Elegiste el Modulo o Resto \n")
    numero = int(input("Introduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print("El resultado es: '", numero, "'")
else:
    print("Tu numero no esta entre los deseados.")

