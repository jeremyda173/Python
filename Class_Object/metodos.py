#Metodos

class Matematica:
    def Suma(self):
        self.n1 = 3
        self.n2 = 4
    
s = Matematica()
s.Suma()
print(s.n1 + s.n2)

#Ejercicio


class Ropa:
    def __init__(self):
        self.marca = 'Messi'
        self.talla = 'M'
        self.color = 'Alegria'

Camisa = Ropa()
print(Camisa.talla)
print(Camisa.color)



class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(8, 5)
print(operacion.producto)  #Se pueden usar todas las operaciones de nuestra calculadora


        