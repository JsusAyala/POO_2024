# Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

tabla=int(input("Ingresa un numero para calcular su tabla de multiplicar"))

i=1
multi=0
print(f"Esta es la tabla del {tabla}")
while i <=10:
    multi=i*tabla
    print(f"{tabla} X {i} = {multi}")
    i+=1