# Tips sobre python...

print(type("Hello Jeremy"))
print("Hello Jeremy")

myStr = "Hola Davo"
# print(type(myStr))  # Es un string

# Convertir a mayúsculas o minúsculas

print(myStr.upper())   # HOLA DAVO
print(myStr.lower())   # hola davo

# Contar la cantidad de letras en una cadena
print(len(myStr)) # 9
# Obtener el primer carácter de una cadena
print(myStr[0]) # H
# Obtener una parte de la cadena, entre dos posiciones (inclusive)
print(myStr[2:6]) # ola D
# Usando el capitalize
print(myStr.capitalize()) # Hello davo
# Usando swapcase
print(myStr.swapcase()) # hOLA dAVO
# Reemplazando partes de mi String
print(myStr.replace("Davo", "Jeremys"))
# Contando caracteres
print(myStr.count("o"))
# Preguntas a mi String
print(myStr.startswith("hello"))
print(myStr.endswith("davo"))
# Metodo split
print(myStr.split())
print(myStr.split(','))
# Buscar un indice
print(myStr.find('o'))
# Buscar longitud
print(len(myStr))
