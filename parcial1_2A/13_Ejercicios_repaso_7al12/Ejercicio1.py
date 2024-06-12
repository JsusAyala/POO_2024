"""
1.- 
 Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado
"""

numeros=[100,25,83,74,45,66,73,28]

#  a.- Recorrer la lista y mostrarla
def recorrer_num():
    for numero in numeros:
        print(numero)

#recorrer_num()

# b.- hacer una funcion que recorra la lista de numeros y devuelva un string
def num_str():
    str_num=str(numeros)
    return str_num
        
num_str()

# c.- ordenarla y mostrarla
def orden_num():
    numeros.sort()
    print(numeros)

#orden_num()

# d.- mostrar su longitud

def longitud_num():
    print(len(numeros))

#longitud_num()

# e.- buscar algun elemento que el usuario pida por teclado

def buscar_num():
    buscar=input("Ingrese el numero a buscar: ") in numeros
    print(buscar)

#buscar_num()