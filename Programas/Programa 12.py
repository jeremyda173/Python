#Operadores logicos

# not o Negacion
# or o Disyuncion
# and o Conjuncion

numero1 = int(input("Escribe un numero mayor a 10 y menor que 50: "))

if numero1 > 10 and numero1 < 50 :
    print("El numero es", numero1, "y cumple con la condicion. \n")
else :
    print("El numero es", numero1, "y no se encuentra entre los los numeros deseados. \n")
    
    
palabra = input("Escribe la palabra 'Yes' o 'Si', para estar de acuerdo con el resultado : ")

if palabra == "Yes" or palabra == "Si" :
    print("Gracias por colaborar con nosotros. \n")
else :
    print("Si tu respuesta fue 'Not' o 'No', dinos cual fue el error? \n")
    

numero2 = int(input("Introduce un numero que sea igual a 5: "))

if not numero2 == 5 :
    print("El numero es diferente a 5. \n")
else:
    print("Es igual a 5. \n")