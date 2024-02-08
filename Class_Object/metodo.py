# metodo constructor

class Persona:
    def __init__(self, nombre, edad):  # metodo constructor de la clase persona
        self.nombre = nombre   # atributo nombre de la clase persona
        self.edad = edad       # atributo edad de la clase persona
    def descripcion(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."
    def comentario(self, frase):
        return f"{frase}, {self.descripcion()}"
# creando una instancia de la clase persona llamada "persona1" con los valores "Juan"
persona1 = Persona("Juan", 25)
print(persona1.nombre)      # accediendo al atributo nombre de persona1
print(persona1.edad)         # accediendo al atributo edad de persona1
print(persona1.descripcion())  # invocando el método descripción para mostrar información completa de persona1
print(persona1.comentario("Hola"))     # invocando el método comentario para agregar un comentario a la descripción de personal

 #modificar un articulo

class Email:
    def __init__(self):
        self._enviado = False
