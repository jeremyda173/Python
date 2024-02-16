# Encapsulacion

class Clienta:
    def __init__(self):
        self.__codigo = 4321

    def __cuenta(self):
        print("Cuenta de procesamiento")

    def getcodigo(self):
        return self.__codigo
    
persona = Clienta()
#objeto._nombreclase__nombre atributo
print(persona._Clienta__codigo)