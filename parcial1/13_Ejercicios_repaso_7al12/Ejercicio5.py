# Crear una lista y un diccionario con el contenido de esta tabla: 

# ACCION              TERROR        DEPORTES
# MAXIMA VELOCIDAD    LA MONJA       ESPN
# ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
# RAPIDO Y FURIOSO I  LA MALDICION   ACCION
# imprimir la información


mi_lista = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]


mi_diccionario = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

print("Lista:")
for fila in mi_lista:
    print(fila)

print("\nDiccionario:")
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")