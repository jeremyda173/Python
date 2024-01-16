#Programa para determinar cual numero es mayor

Numero1 = int(input("Introduce el primer numero: \n"))
Numero2 = int(input("Introduce el segundo numero: \n"))
Numero3 = int(input("Introduce el tercer numero: \n"))
              
if  Numero1 < Numero2 > Numero3 :
              print("\n El numero '", Numero2 ,"' es el mayor osea, el segundo numero. \n")
elif Numero2 < Numero1 > Numero3 :
              print("\n El numero '", Numero1 ,"' es el mayoro osea, el primer numero. \n")
elif Numero1 < Numero3 > Numero2 :
              print("\n El numero '", Numero3 ,"' es el mayor osea, el tercer numero. \n")
else:
    print("Son todos iguales.")