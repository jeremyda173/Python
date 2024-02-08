#class and objects 1 and 2

class Persona:
    doctor = 'Rafael'

print(Persona.doctor)


class Jugador:
    j1 = 'Messi'
    j2 = 'CR7'
    j3 = 'Neymar'
    
print(Jugador.j1)

class Jugadores_B:
    j4 = 'Marcelo'
    j5 = 'Ramos'
    j1 = 'Falcao'
    
print(Jugadores_B.j1)


class Equipos:
    Team1 = 'Barcelona'
    Team2 = 'Real Madrid'
    Team3 = 'Liverpool'

print("Cual es el mejor equipo? \n" + Equipos.Team1)


#Ejercicio

class Nombre:
    pass

Victor = Nombre()
Juan = Nombre()

#objeto.atributo = valor

Victor.edad = 32
Victor.peso = "320 Libras"
Victor.genero = "Masculino"

Juan.edad = 45
Juan.peso = "128 Libras"
Juan.genero = "Masculino"

print(Victor.edad)
print(Juan.peso)
