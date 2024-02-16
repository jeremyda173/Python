# metodo super()

class Mamifero:
    def __init__(self, nombre):
        print(nombre, 'es un animal de sangre fria')

class Leon(Mamifero):
    def __init__(self):
        print('el leon es un animal de cuatro patas')
        super().__init__("León")  # Llamada al método init de la clase padre con el argumento "León"

nuevo_leon = Leon()