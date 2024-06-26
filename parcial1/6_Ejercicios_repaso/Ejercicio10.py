#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

contador=1
reprobados=0
aprobados=0
error=0
while contador<=15:
    calif = float(input(f"Ingresar la calificacion del alumno {contador}: "))
    contador+=1
    if calif <= 7.9:
        print("Reprobo")
        reprobados+=1
    if calif >= 8 and calif <= 10:
        print("Aprobo")
        aprobados+=1
    if calif >= 10.1:
        print("Calificacion invalida")
        error+=1
print(f"Los estudiantes que aprobaron fueron {aprobados} y los estudiantes que reprobaron son {reprobados}.")
if error >= 1:
   print(f"Hay un total de {error} calificaciones invalidas favor de verificar en rectoria.")