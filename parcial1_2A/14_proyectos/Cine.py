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
def vaciarPeliculas():
    peliculas.clear()
    print("Se han eliminado con exito las peliculas de todo el catalogo")


peliculas=[]

opcion=True
while opcion:
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestion de Peliculas:::...\n 1.- Agregar \n 2.- Eliminar \n 3.- Remover \n 4.-Actualizar \n 5.- Consultar \n 6.- Vaciar \n 7.- Salir ")
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
    elif opcion=="6" or opcion=="VACIAR":
        vaciarPeliculas()
    elif opcion=="7" or opcion=="SALIR":
        opcion=False

    else:
        print("Opcion invalida \n Favor ingresar una opcion valida")
        espereTecla()