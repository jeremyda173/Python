'''Solicitar un libro prestado en la biblioteca de la Universidad.'''
print("Hola, este algoritmo trata sobre determinar si puedo tomar un libro prestado\n")

Libro = [201, "Los 2 cerditos", "2$"]

if Libro:
    print("Hola, aqui tienes tu libro:")
    print(f"ID: {Libro[0]}")
    print(f"Título: {Libro[1]}")
    print(f"Precio: {Libro[2]}")
else:
    print("Hola, no hay libros disponibles")

print("Pase buen dia...")


