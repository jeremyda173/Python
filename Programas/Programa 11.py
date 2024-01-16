#Operadores relacionales

'''
>
<
<=
>=
!=
==
'''
#Ejercicio

Numero_1 = int(input("Introduce el primer numero: \n"))
Numero_2 = int(input("Introduce el primer numero: \n"))

print("____________________________")
if Numero_1 > Numero_2 :
    print("Estos numeros no son iguales:", Numero_1, "!=", Numero_2)
    print("El primer numero es mayor:", Numero_1, ">", Numero_2)
elif Numero_1 == Numero_2 :
    print("Estos numeros son iguales:", Numero_1, "==", Numero_2)
else:
    print("Estos numeros no son iguales:", Numero_1, "!=", Numero_2)
    print("El segundo numero es mayor:", Numero_1, "<", Numero_2)
print("____________________________")