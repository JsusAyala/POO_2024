#1.- Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente:
#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado
#1
# numero = [9,4,3,17,2,6,12,8]

# def recorrer_lista(lista):
#     for numero in lista:
#         print (f"Esta es la lista Recorrida: {numero}")

# def lista_como_string(lista):
#     return " ".join(map(str, lista))

# def ordenar_lista(lista):
#     lista.sort()
#     return lista

# def longitud_lista(lista):
#     len(lista)
#     return
 
# def buscar_numero(lista,numeros):
#     numeros = int(numeros)
#     if numeros in lista:
#      indice = numero.index(lista)
#      return()
    
    
# recorrer_lista(numero)
# lista_como_string(numero)
# longitud_lista(numero)
# buscar_numero(numero)

numero = [9, 3, 4, 17, 2, 6, 12, 8]

def recorrer_lista(lista):
    for num in lista:
        print(num)

def lista_como_string(lista):
    return " ".join(map(str, lista))

def ordenar_lista(lista):
    numero.sort(lista)
    return lista

def longitud_lista(lista):
    return len(lista)

def buscar_numero(lista, numero_a_buscar):
    if numero_a_buscar in lista:
        indice = lista.index(numero_a_buscar)
        print(f"El número {numero_a_buscar} se encuentra en el índice {indice+1}")
    else:
        print(f"El número {numero_a_buscar} no se encuentra en la lista")

recorrer_lista(numero)
print(f"Este es el ordem de la lista: {ordenar_lista}")
print("Lista como cadena:", lista_como_string(numero))
print("Longitud de la lista:", longitud_lista(numero))
numero_a_buscar = int(input("Introduce el número que deseas buscar: "))
buscar_numero(numero, numero_a_buscar)




















































































