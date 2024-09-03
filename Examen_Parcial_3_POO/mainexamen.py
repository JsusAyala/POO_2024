from Clases.funciones import *
import os 
import getpass

def menu_login():
    while True:    
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            obj_usurio=Usuario(nombre,apellidos,email,password)
            resultado=obj_usurio.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...")  
            esperarTecla()      
        elif opcion == '2' or opcion=="LOGIN":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            registro=Usuario.iniciar_sesion(email,password)
            if registro:
                menuPrincipal(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
                esperarTecla()    
        elif opcion == '3' or opcion=="SALIR":
            print("\n\t.. ¡Gracias Bye! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menuPrincipal(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Agencia de Autos ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()
        if opcion=='1':
            os.system("cls")
            print("...::Autos::...")
            print(" 1. Añadir un auto\n 2. Mostrar autos \n 3. Actualizar autos \n 4. Eliminar autos \n 5. Salir")
            opcion1 = input("Seleccione una opción: ")

            if opcion1 == '1':
                os.system("cls")
                print("...::Añadir un auto::...")
                matricula = input("Ingrese la matrícula: ")
                marca = input("Ingrese la marca: ")
                modelo = input("Ingrese el modelo: ")
                color = input("Ingrese el color: ")
                nif = input("Ingrese el NIF: ")
                objetoAuto = Auto(matricula, marca, modelo, color, nif)
                objetoAuto.crear()
                esperarTecla()
                os.system("cls")

            elif opcion1 == '2':
                os.system("cls")
                print("..::Mostrar autos::..")
                resultados = Auto.mostrar()
                if resultados:
                    for resultado in resultados:
                        print(f" Matrícula: {resultado[0]}\n Marca: {resultado[1]}\n Modelo: {resultado[2]}\n Color: {resultado[3]}\n NIF: {resultado[4]}")
                else:
                    print("No se encontró ningún auto.")
                esperarTecla()
                os.system("cls")

            elif opcion1 == '3':
                Auto.actualizar()
                esperarTecla()

            elif opcion1 == '4':
                matricula = input("\t \t Matrícula del auto a eliminar: ")
                resultado = Auto.eliminar(matricula)
                if resultado:
                    print(f"\n \t \t.::Auto Eliminado Correctamente ::.")
                else:
                    print(f"\n \t \t** No fue posible eliminar el auto ... vuelva a intentarlo **...")
                esperarTecla()

            elif opcion1 == '5':
                break

            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

        elif opcion=='2':
            os.system("cls")
            print("...::Clientes::...")
            print(" 1. Añadir un cliente\n 2. Mostrar clientes \n 3. Actualizar clientes \n 4. Eliminar clientes \n 5. Salir")
            opcion2=input("Seleccione una opción: ")
            if opcion2=='1':
                os.system("cls")
                print("...::Añadir un cliente::...")
                nombre=input("Ingrese su nombre: ") 
                apellido=input("Ingrese su apellido: ")
                email=input("Ingrese su email: ")
                telefono=input("Ingrese su número de teléfono: ")
                direccion=input("Ingrese su dirección: ")
                objetocliente=cliente(id, nombre, apellido, email, telefono, direccion)
                objetocliente.crear()
                esperarTecla()
                os.system("cls")
            elif opcion2=='2':
                os.system("cls")
                print("..::Mostrar clientes::..")
                resultados = cliente.mostrar()
                if resultados:
                    for resultado in resultados:
                        print(f" ID: {resultado[0]}\n Nombre: {resultado[1]}\n Apellido: {resultado[2]}\n Email: {resultado[3]}\n Teléfono: {resultado[4]}\n Dirección: {resultado[5]}")
                else:
                    print("No se encontró ningún cliente con ese ID.")
                esperarTecla()
                os.system("cls")
            elif opcion2=='3':
                cliente.actualizar()
            elif opcion2=='4':
                id = input("\t \t ID del cliente a eliminar: ")
                resultado=cliente.eliminar(id)
                if resultado:
                    print(f"\n \t \t.::Cliente Eliminado Correctamente ::.")
                else:
                    print(f"\n \t \t** No fue posible eliminar al cliente ... vuelva a intentarlo **...")  
                esperarTecla()
            elif opcion2=='5':
                exit
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                esperarTecla()
        
        elif opcion=='3':
            while True:
                os.system("cls")
                print("...::Revisiones::...")
                print(" 1. Añadir una revisión\n 2. Mostrar revisiones \n 3. Actualizar revisión \n 4. Eliminar revisión \n 5. Salir")
                opcion3 = input("Seleccione una opción: ")

                if opcion3 == '1':
                    os.system("cls")
                    print("...::Añadir una revisión::...")
                    no_revision = input("Ingrese el número de revisión: ")
                    cambiofiltro = input("¿Cambio de filtro? (Sí/No): ")
                    cambioaceite = input("¿Cambio de aceite? (Sí/No): ")
                    cambiofreno = input("¿Cambio de freno? (Sí/No): ")
                    otros = input("Otros cambios: ")
                    matricula = input("Ingrese la matrícula del vehículo: ")
                    objeto_revision = Revisiones(id, no_revision, cambiofiltro, cambioaceite, cambiofreno, otros, matricula)
                    objeto_revision.crear()
                    esperarTecla()
                    os.system("cls")

                elif opcion3 == '2':
                    os.system("cls")
                    print("..::Mostrar revisiones::..")
                    resultados = Revisiones.mostrar()
                    if resultados:
                        for resultado in resultados:
                            print(f" ID: {resultado[0]}\n No. Revisión: {resultado[1]}\n Cambio de Filtro: {resultado[2]}\n Cambio de Aceite: {resultado[3]}\n Cambio de Freno: {resultado[4]}\n Otros: {resultado[5]}\n Matrícula: {resultado[6]}")
                    else:
                        print("No se encontró ninguna revisión.")
                        esperarTecla()
                    os.system("cls")

                elif opcion3 == '3':
                    Revisiones.actualizar()

                elif opcion3 == '4':
                    id = input("ID de la revisión a eliminar: ")
                    resultado = Revisiones.eliminar(id)
                    if resultado:
                        print("\nRevisión eliminada correctamente.")
                    else:
                        print("\n** No fue posible eliminar la revisión... vuelve a intentarlo **...")
                    esperarTecla()

                elif opcion3 == '5':
                    break

                else:
                    print("\nOpción no válida. Intenta de nuevo.")
                    esperarTecla()

        elif opcion=='5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
  menu_login()
