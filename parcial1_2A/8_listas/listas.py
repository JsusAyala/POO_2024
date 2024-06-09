"""

List Array
son colecciones o un conjunto de datos/valores bajo
un mismo nombre, para acceder a los valores se
hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite miembros duplicados.


"""

#Ejemplo 1 Crear una lista con valores numericos enteros e imprimir la lista
"""
numeros=[23,34]
print(numeros)
"""
#Recorrer la lista con un for
"""
for i in numeros:
    print(i)
"""
#Recorrer la lista con un while
"""
i=0
while i<len(numeros):
    print(numeros[i])
    i+=1
"""
#Ejemplo 1 Crear una lista  de palabras , posteriormente ingresar una palabra para buscar la coincidencia en lista. E indicar di aparece la palabra y en que posicion en caso contrario indicar una sola vez si no la encontro
"""
palabras=["hola","2024","10.23","True"]

palabra_buscar=input("Ingresa la palabra a buscar: ")

noencontro=True
"""
#for i in palabras:
#    if palabra_buscar==i:
#        print(f"Encontre la palabra {palabra_buscar}, en la posicion: {palabras.index(i)} ")
#        noencontro=False
"""
while i<len(palabras):
    if palabra_buscar==palabras[i]:
        print(f"Encontre la palabra {palabra_buscar}, en la posicion: {i} ")
        if noencontro:
            print(f"No se encontro la palabra dentro de la lista")
"""
#ejemplo 2 crear una lista de palabras posteriormente ingresar una palabra para buscar la coincidencia en la lista e indicar 
#si aparece la palabra y en que posicion en caso contrario indicar una sola vez si no la encontro

"""
#palabra_buscar = input ("ingresar la palabra a buscar: ")
palabra = [ "hola", "2024" , "10.23","True"]
palabra_buscar = input ("ingresar la palabra a buscar: ")
#Recorrer la lista con un for 
"""
#Recorrer la lista con un 



# palabra = [ "hola", "2024" , "10.23","True"]
# palabra_buscar = input ("ingresar la palabra a buscar: ")


# noloencontro = True

# for o in palabra : 
#     if  palabra_buscar == o:
     
#      print (f"Encontre la palabra {palabra_buscar}, en la posicion : {palabra.index (o)}")
#      noloencontro = False 


# if noloencontro:
#  print(f"no se encontro la palabra dentro de la lista ")



# print ("\n") 

# print ("esto es con el while")

# print ("\n") 

# #Recorrer la lista con un while

# palabra = [ "hola", "2024" , "10.23","True"]
# palabra_buscar = input ("ingresar la palabra a buscar: ")

# while  o <len (palabra):
#     if palabra == palabra_buscar [o]:
#      print (f"Encontre la palabra {palabra_buscar}, en la posicion : {palabra.index (o)}")
#      noloencontro = False 
#     o+=1
        
        
# if noloencontro:
#  print(f"no se encontro la palabra dentro de la lista ")
    


#Ejemplo 3  lsitas multilineal o multidimensional (matriz) para crear una agenda
"""
nombres = [
    ["Carlos" , 6181234567],
    ["Fernando", 6182334567],
    ["Matiaas", 6691112233],
    ["Juan", 6182332345]
]
print (nombres)

for o in nombres:
    print (f"{nombres.index(o)+1}.-{o}")

"""
#Ejemplo 4 Crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas
#Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombre de peliculas

def espereTecla():
    print("Oprima cualquier tecla para continuar")    
    input()    
def insertarPeliculas():
    print("Este es el listado de peliculas disponibles: ")
    print(peliculas)
    pelicula=input("Ingrese la pelicula que se agregara: ")
    peliculas.append(pelicula)
    espereTecla()
def eliminarPeliculas():
    print("Este es el listado de peliculas disponibles: ")
    print(peliculas)
    pelicula=input("Ingrese la pelicula que se eliminara: ")
    if pelicula == peliculas:
        peliculas.remove(pelicula)
        print("La pelicula fue eliminada exitosamente")
        espereTecla()
    else:
        print("La película no existe en la lista.")
        espereTecla()
def removerPeliculas():
    print("Este es el listado de peliculas disponibles1: ")
    print(peliculas)
    pelicula=input("Ingrese la posicion de la pelicula que sera removida: ")
    if pelicula == peliculas:
        peliculas.pop(pelicula)
        print("La pelicula fue removida exitosamente")
        espereTecla()
    else:
        print("La película no existe en la lista.")
        espereTecla()
def consultarPeliculas():
    print("Este es el listado de peliculas: ")
    print(peliculas)
    espereTecla()
def actualizarPeliculas():
    print("Este es el listado de peliculas: ")
    print(peliculas)
    pelicula_actual = input("Ingrese el nombre de la película que sera actualizada: ")
    if pelicula_actual in peliculas:
        indice = peliculas.index(pelicula_actual)
        nueva_pelicula = input("Ingrese el nuevo nombre de la película: ")
        peliculas[indice] = nueva_pelicula
        print("Película se actualizo correctamente.")
    else:
        print("La película no existe en la lista.")
    espereTecla()

peliculas=[]

opcion=True
while opcion:
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestion de Peliculas:::...\n 1.- Agregar \n 2.- Eliminar \n 3.- Remover \n 4.-Actualizar \n 5.- Consultar \n 6.- Salir ")
    opcion=input("\t Elige una opción: ").upper()
    
    if opcion=="1" or opcion=="AGREGAR":
        insertarPeliculas()
    elif opcion=="2" or opcion=="ELIMINAR":
        eliminarPeliculas()
    elif opcion=="3" or opcion=="REMOVER":
        removerPeliculas()
    elif opcion=="4" or opcion=="ACTUALIZAR":
        actualizarPeliculas()
    elif opcion=="5" or opcion=="CONSULTAR":
        consultarPeliculas()
    elif opcion=="6" or opcion=="SALIR":
        opcion=False
    else:
        print("Opcion invalida \n Favor ingresar una opcion valida")
        espereTecla()