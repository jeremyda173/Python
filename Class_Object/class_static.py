# Clase y estatico

class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    def __repr__(self):
        return f"Pastel({self.ingredientes})"
    @classmethod
    def Pastel_chocolate(cls):
        return cls(['chocolate', 'azucar'])
    @classmethod
    def Pastel_vainilla(cls):
        return cls(['vainilla', 'miel'])

print(Pastel.Pastel_chocolate())  # Devuelve: Pastel(['chocolate', 'azucar])
print(Pastel.Pastel_vainilla())   # Devuelve: Pastel(['vainilla', 'miel])

# Estatico 