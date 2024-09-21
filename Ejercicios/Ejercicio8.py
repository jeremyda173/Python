# Entrada
letra1 = input("Ingrese la primera letra mayúscula: ")
letra2 = input("Ingrese la segunda letra mayúscula: ")

# Validación
if not (letra1.isupper() and letra2.isupper()):
    print("Las letras deben ser mayúsculas.")
elif letra1 >= letra2:
    print("La primera letra debe ser menor que la segunda.")
else:
    # Imprimir letras
    for i in range(ord(letra1) + 1, ord(letra2)):
        print(chr(i), end='')
    print()
