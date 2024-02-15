# Herencia practica, calculadora donde se puedan introducir datos reales

# Example 1

'''class Calculadora:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    
    def set_valores(self, num1, num2):
        """Asigna los valores a las variables de la clase"""
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            self.num1 = num1
            self.num2 = num2
        else:
            raise ValueError("Los valores deben ser números")
            
    def sumar(self):
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
        
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        if self.num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        else:
            return self.num1 / self.num2

# Creando una nueva clase que hereda de Calculadora y agregándole un método adicional llamado "potencia"
class CalculadoraAvanzada(Calculadora):
    def potencia(self):
        return self.num1 ** self.num2

calc = Calculadora()
print(calc.set_valores(5, 3).sumar())   # Imprime 8
print(calc.set_valores(7, 2).restar())  # Imprime 5
print(calc.set_valores(9, 4).multiplicar())   # Imprime 36
try:
    print(calc.divi)  # Llamado al método no existente en la clase base
except AttributeError as e:
    print(e)  # Imprime el mensaje de error

calcavanzada = CalculadoraAvanzada()
print(calcavanzada.set_valores(2, 4).potencia())'''  # Imprime 16

#Example 2

'''class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos numeros"""
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        """Resta de dos numeros"""
        self.resultado = a - b
        return self.resultado


class CalculadoraAritmetica(Calculadora):
    """Clase que extiende la clase Calculadora y agrega funcionalidad aritmética adicional."""

    def multiplicar(self, a, b):
        """Multiplica dos numeros"""
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        """Divide un numero entre otro"""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        else:
            self.resultado = a / b
            return self.resultado


# Creando objetos de las clases
calc_basica = Calculadora()
calc_aritmetica = CalculadoraAritmetica()

print("Resultado de calc_basica.sumar(2,3) :", calc_basica.sumar(2, 3))
print("Resultado de calc_aritmetica.multiplicar(4 + 5) :", calc_aritmetica.multiplicar(4, 5))

try:
    print("Resultado de calc_aritmetica.dividir(8,0) :", calc_aritmetica.dividir(8, 0))
except ValueError as e:
    print("Se ha producido el error esperado: ", e)'''

# Example 3


class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for _ in range(numero)]

    def ingresardato(self):
        self.datos = [int(input('Ingrese dato numero ' + str(i + 1) + ': ')) for i in range(self.n)]
        return self.datos

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b = self.datos
        s = a + b
        print('El resultado de la suma =', s)

    def resta(self):
        a, b = self.datos
        r = a - b
        print('El resultado de la resta = ', r)

class op_normales(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def Cuadrada(self):
        import math
        a, = self.datos
        print('El resultado de la cuadratura es= ', math.sqrt(a))

ejemplo = op_basicas()
ejemplo.ingresardato()
ejemplo.suma()


objeto = op_basicas() # Verificando las herencias
print(isinstance(objeto, op_basicas)) # Metodo de comprobacion de herencias.

print(issubclass(Calculadora, op_basicas)) # Devuelve un false
print(issubclass(op_basicas, Calculadora))  # Devuelve un True
'''La primera es la subclase y la segunda es la clase padre'''


    
        