#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

num1 = int(input("Ingresar el porcentaje: "))
num2 = int(input("Ingrese el número: "))

porcentaje=(num1*num2)/100

print(f"{porcentaje} es el {num1} por ciento de {num2}")