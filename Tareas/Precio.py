'''Incrementar precio, se trata de un algoritmo que al leer un precio le aumente un 15% del valor original  (Algoritmo del tipo cuantitativo).'''
print("Hola, este algoritmo trata sobre determinar el precio mas 15%\n")

def increment_precio(precio):
    incremento = precio * 0.15
    new_precio = precio + incremento
    return new_precio

precio_ori = float(input("Introduce el precio original: "))
precio_increment = increment_precio(precio_ori)
print(f"El precio incrementado en un 15% es: {precio_increment:.2f}")


