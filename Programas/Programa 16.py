# Bucle while con sentencias Break or Continue


#Break

contador = -1

while contador < 10:
    contador += 1
    
    if contador == 7:
        break # Al usar un break estoy haciendo que el ciclo cuente hasta 10 pero, cuando encuentre el 7 se detenga.
    print("Valor del contador sera: ", contador)
    
print("Ahora a ver el continue \n") 
#Continue

contador = -1

while contador < 10:
    contador += 1
    
    if contador == 7:
        continue # Al usar un break estoy haciendo que el ciclo cuente hasta 10 pero, cuando encuentre el 7 se detenga.
    print("Valor del contador sera: ", contador)