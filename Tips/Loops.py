# Cliclos FOR and WHILE

'''El ciclo while se utiliza cuando no se conoce de antemano cuántas veces se ejecutará el bloque de código, pero se ejecutará mientras la condición sea verdadera. '''
'''El ciclo for se utiliza cuando se conoce de antemano la cantidad de veces que se desea ejecutar el bloque de código.'''

foods = ['apples', 'bread', 'cheese']

list = list(range(1, 21))
print("Lista de numeros del uno al veinte: ", list)

fruit_list = [   
    {'name': 'apple', 'color': 'red'},
    {'name': 'banana', 'color': 'yellow'}
   ]

veggie_list = [
    {'name':'broccoli','family':'brassica' },
    {'name':'carrot','family':'dicotyledonous' }
]

for num in list:
    if num % 2 == 0:
        print ("El numero",num,"es par")
    else:
        print ("El numero",num,"es impar")

for food in foods:
    if food == "bread":
        print("I can't eat it's")  # break
    print("\n" + food)
