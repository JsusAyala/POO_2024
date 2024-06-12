"""
 Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
 y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones
"""

def imprimir_tipo(variable):
    if isinstance(variable, list):
        print(f"La variable '{variable}' es una lista.")
    elif isinstance(variable, str):
        print(f"La variable '{variable}' es una cadena.")
    elif isinstance(variable, int):
        print(f"La variable '{variable}' es un entero.")
    elif isinstance(variable, bool):
        print(f"La variable '{variable}' es un lógico.")
    else:
        print(f"La variable '{variable}' tiene un tipo desconocido.")

lista = [1, 2, 3, 4]
cadena = "Hola, mundo"
entero = 42
logico = True

imprimir_tipo(lista)
imprimir_tipo(cadena)
imprimir_tipo(entero)
imprimir_tipo(logico)
