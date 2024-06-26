# 3.- Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
# palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
# el contenido de la lista en mayusculas

lista = []

if not lista:
    print (f"No hay ningun elemento en esta lista. Vamos a llenar esta lista")

while True:
    lista_vacia = input("Introdusca cualquier palabra o frase,(o 'salir' para terminar): ")
    
    if lista_vacia.lower() == "salir": 
        break
    palabras = lista_vacia.split()
    lista.extend(palabras)



for lista2 in lista:
    print(lista2.upper())














