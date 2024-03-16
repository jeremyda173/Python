
import tkinter as tk #Es una biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI).

def convertir():
    numero = entrada.get()
    sistema_origen = lista_origen.get()
    sistema_destino = lista_destino.get()
    
    if sistema_origen == 'Decimal':
        numero_decimal = int(numero)
    elif sistema_origen == 'Binario':
        numero_decimal = int(numero, 2)
    elif sistema_origen == 'Octal':
        numero_decimal = int(numero, 8)
    elif sistema_origen == 'Hexadecimal':
        numero_decimal = int(numero, 16)
    
    if sistema_destino == 'Decimal':
        resultado.set(numero_decimal)
    elif sistema_destino == 'Binario':
        resultado.set(bin(numero_decimal)[2:])
    elif sistema_destino == 'Octal':
        resultado.set(oct(numero_decimal)[2:])
    elif sistema_destino == 'Hexadecimal':
        resultado.set(hex(numero_decimal)[2:].upper()) #Se utiliza para convertir una cadena de texto a letras mayúsculas.

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Convertidor de Sistemas Numéricos")

# Etiqueta de entrada
tk.Label(root, text="Número:").grid(row=0, column=0, padx=5, pady=5)

# Campo de entrada
entrada = tk.Entry(root)
entrada.grid(row=0, column=1, padx=5, pady=5)

#Una Lista desplegando los sistemas numéricos de origen
lista_origen = tk.StringVar(root)
lista_origen.set("Decimal")
tk.OptionMenu(root, lista_origen, "Decimal", "Binario", "Octal", "Hexadecimal").grid(row=0, column=2, padx=5, pady=5)

#Una Lista desplegando los sistemas numéricos de destino
lista_destino = tk.StringVar(root)
lista_destino.set("Decimal")
tk.OptionMenu(root, lista_destino, "Decimal", "Binario", "Octal", "Hexadecimal").grid(row=0, column=3, padx=5, pady=5)

#Botón de conversión
tk.Button(root, text="Convertir", command=convertir).grid(row=0, column=4, padx=5, pady=5)

#Etiqueta de resultado
resultado = tk.StringVar()
tk.Label(root, text="Resultado:").grid(row=1, column=0, padx=5, pady=5)

#Campo de resultado (solo lectura)
tk.Entry(root, textvariable=resultado, state="readonly").grid(row=1, column=1, columnspan=4, padx=5, pady=5)

root.mainloop() #Inicia el bucle principal de la interfaz gráfica.
