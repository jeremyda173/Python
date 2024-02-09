#Funciones para atributos

class Persona:
    edad = 21
    nombre = "Juan"
    pais = "Puerto Rico"
    
doctor = Persona()
print("Los datos del doctor son: ", doctor.nombre, doctor.edad)

print("Los datos del doctor son: ", getattr(doctor, 'edad')) #Atributo 1 GETATTR

print("El doctor tiene edad? ", hasattr(doctor, 'edad')) #Atributo 2 HASATTR

print('antes era: ', doctor.nombre)
setattr(doctor, 'nombre', 'Pedro') #Atributo 3 SETATTR
print('ahora es: ', doctor.nombre)

#delattr(Persona, 'pais') #Atributo 4 DELATTR
print(doctor.pais)

