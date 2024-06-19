'''Determinar la distancia recorrida de un vehículo, importante, la velocidad y el tiempo deben ser datos de entrada, es decir, puede funcionar para determinar cualquier distancia por lo qué las variables velocidad y tiempo no pueden ser en base a un valor fijo (Algoritmo del tipo cuantitativo).'''
print("Hola, este algoritmo trata sobre determinar la distancia de un vehiculo\n")

velocidad = float(input("Introduce la velocidad del vehículo (en km/h): "))
time = float(input("Introduce el tiempo (en horas): "))

def calcular_distancia(velocidad, time):
    return velocidad * time

distancia = calcular_distancia(velocidad, time)

print(f"La distancia recorrida por el vehiculo es de: {distancia:.2f} km")

