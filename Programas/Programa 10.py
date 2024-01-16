print("========")
print("Conversor")
print("======== \n")

print("Menu de opciones: \n")
print("Preciona 1 para convertir de numero a palabra")
print("Preciona 2 para convertir de palabra a numero \n")

opcion = int(input("Cual es tu opcion? "))

if opcion == 1:
    print("Elegiste convertir de numero a palabra.")
    
    opcion_1 = int(input("\n Que numero deseas convertir? \n"))
    
    if opcion_1 == 0:
        print("CERO")
    elif opcion_1 == 1:
           print("UNO")
    elif opcion_1 == 2:
        print("DOS")
    elif opcion_1 == 3:
        print("TRES")
    elif opcion_1 == 4:
        print("CUATRO")
    elif opcion_1 == 5:
        print("CINCO")
    else:
        print("Solo se encuentra hasta el 5")
        
elif opcion == 2:
    
      print("\n Elegiste convertir de palabra a numero \n")
      
      opcion_dos = input("\n Que palabra deseas convertir? \n")
      opcion_dos = opcion_dos.lower()
    
      if opcion_dos == "Cero" :
          print("0")
      elif opcion_dos == "uno" :
            print("El numero es: 1")
      elif opcion_dos == "dos":
          print("2")
      elif opcion_dos == "tres":
          print("3")
      elif opcion_dos == "cuatro":
          print("4")
      elif opcion_dos == "jungkook":
          print("8")
      else:
          print("Solo es hasta el 6")
else:
    print("Tu numero no se encuentra entre las opciones")
    
