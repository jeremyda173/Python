#Poliformismo por funcion

class Tomate:
    def tipo(self):
        print('vegetal')
    def color(self):
        print('rojo')

class Manzana:
    def tipo(self):
        print('fruta')
    def color(self):
        print('verde')
        
def funcion(objeto):
    objeto.tipo()
    objeto.color()
nuevo_tomate = Tomate()
nueva_manzana = Manzana()
funcion(nuevo_tomate)
print("---")
funcion(nueva_manzana)


#Polimorfismo con metodo

class Colombia:
    def capital(self):
        print('Capital')
    def idioma(self):
        print('Español')

class Francia:
    def capital(self):
        print('París')
    def idioma(self):
        print('Francés')

class Alemania:
    def capital(self):
        print('Berlín')
    def idioma(self,idioma):
        print(f'Idioma oficial: {idioma}')

colombiano = Colombia()
frances = Francia()
alemano = Alemania()

print("Paises y capitales: ")
for pais in (colombiano, frances, alemano):
    pais.capital()
    pais.idioma()
    

