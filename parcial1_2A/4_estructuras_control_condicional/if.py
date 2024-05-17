"""

existe una estructura de condicion lla mada "if"
la cual evalua una condicion para encontrar el valoe "True" y si se cumple
la condicion se ejecuta la linea o lineas de codigo

tienes 4 variantes de if 

1.-if  simple
2.-if compuesto
3.-if anidado
4.-if y elif

"""

#Ejemplo 1 if simple

color=input("Ingresa un color")

if color == "rojo":
    print("Soymel color rojo")

#Ejemplo 2 if compuesto

color=input("Ingresa un color")

if color == "rojo":
    print("Soymel color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#Ejemplo 3 if anidado

color=input("Ingresa un color")

if color == "rojo":
    print("Soy el color rojo")
    if color!="rojo":
        print("Soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#Ejemplo 4 if y elif

color=input("Ingresa un color")

if color == "rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo")
elif color=="azul":
    print("Soy el color azul")
elif color=="morado":
    print("Soy el color morado")
else:
    print("No soy ningun de los anteriores")

#Ejemplo 5 crear un programa que solicite el numero de la semana e imprima en pantalla el dia que le corresponde

dia=input("Ingresa un numero del 1 al 7 para ver el dia de la semana")

if dia == "1":
    print("Lunes")
elif dia=="2":
    print("Martes")
elif dia=="3":
    print("Miercoles")
elif dia=="4":
    print("Jueves")
elif dia=="5":
    print("Viernes")
elif dia=="6":
    print("Sabado")
elif dia=="7":
    print("Domingo")
else:
    print("Opcion invalida por favor ingrese una opcion valida")
