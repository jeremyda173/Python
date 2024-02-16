# Herencia multiple

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("Llamando a un teléfono")
    def ocupado(self):
        print("Ocupado")

class Camara:
    def __init__(self):
         pass
    def tomar_foto(self):
        print ("Tomando foto de una camara")

class Reproduccion:
    def __init__(self):
        pass
    def reproducirMusica(self):
        print("Reproduciendo musica")
    def reproducirVideo(self):
        print("Reproduciendo video")

class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print("Telefono apagado")


movil = Smartphone()
# print (dir(movil))
# print(movil.fotografia())
print(movil.llamar())
# print(movil.tomar_foto())
# print(movil.ocupado())