# Creando una lista capaz de:

# Crear la list
list = list(range(1, 21))
print("Lista de numeros del uno al veinte: ", list)
# Buscando un elemento en la lista
numero_buscar = int(input("Ingrese el numero que desea buscar en la lista: "))
if numero_buscar in list:
    print("El numero", numero_buscar, "se encuentra en la lista")
else:
    print("El numero", numero_buscar, "no se encuentra en la lista")
# Agregar elementos a la lista
agregar = int(input("Ingrese un numero para agregarlo a la lista y presione enter: "))
list.append(agregar)
print("Nueva lista con el numero agregado: ", list)
\
# Eliminar un elemento de la lista
eliminar = int(input("Ingresa el numero que deseas eliminar de la lista y presiona Enter: "))
list.remove(eliminar)
print("Nueva lista sin el numero eliminado: ", list)