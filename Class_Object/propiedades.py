#propiedades()

class Empleados:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    def __getnombre(self):
        return self.__nombre
    def __getapellido(self):
        return self.__apellido
    def __getedad(self):
        return self.__edad
    
    def __setnombre(self, nombre):
        self.__nombre = nombre
    def __setapellido(self, apellido):
        self.__apellido = apellido
    def __setedad(self, edad):
        self.__edad = edad

    def __delnombre(self):
        del self.__nombre
    def __delapellido(self):
        del self.__apellido
    def __deledad(self):
        print("No se puede eliminar la edad")    

    nombre = property(fget= __getnombre,
                      fset= __setnombre,
                      fdel= __delnombre,
                      doc = "soy la propiedad del 'nombre'")
    edad = property(fget= __getedad)
empleado_uno = Empleados('Victor',21)
empleado_uno.nombre = 'Sara'
print(empleado_uno.nombre, empleado_uno.edad)

    
        
#Creando un objeto de la clase Empleado
            
# emp1 = Empleados("Juan", "Perez", 25)
# print(emp1.getnombre())
# emp1.setnombre("Luis")
# print(emp1.getnombre())
# #-------------------------------
# emps = [Empleados("Ana", "Garcia", 30), Empleados("Maria", "Rodriguez", 40)]
# for e in emps:
#     print(e.getnombre(), end=" ")
#     print(e.getapellido())

# emp1 = Empleados("Juanito", "Perezosa", 25)
# print(emp1.getedad())
# emp1.setedad(25)
# print(emp1.getedad())