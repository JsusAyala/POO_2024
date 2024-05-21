#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

contador=1
while contador<=15:
    calif = float(input(f"Ingresar la calificacion del alumno {contador}: "))
    contador+=1
    if calif <= 7.9:
        print("Reprobo")
    else:
        print("Aprobo")
    if calif >= 10.1:
        print("Calificacion invalida")