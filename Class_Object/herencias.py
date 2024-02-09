# herencias

class pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)

class goku (pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)
    
class charmander(pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

nuevo_pokemon = goku('boby', 'electrico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('super viento'))

otro_pokemon = charmander('charmmy', 'fuego')
print(otro_pokemon.descripcion())
print(otro_pokemon.ataque('normal'))