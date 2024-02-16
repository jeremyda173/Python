# Poliformismo

class Auto:
    rueda = 4
    def desplazamiento(self):
        print('Auto en movimiento')

class Moto:
    rueda = 2
    def desplazamiento(self):
        print('Moto en movimiento')
        
def viajar(vehiculo, distancia):
    vehiculo.desplazamiento()
    print(f'Se ha recorrido {distancia} km')
    
coche = Auto()
moto = Moto()
viajar(coche, 300)
print("")
viajar(moto, 150)