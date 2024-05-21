# Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo)
# de los 60 primeros numeros naturales. Resolverlo con while y for

i=0
while i <= 60:
    i+=1
    cuadrado = i * i
    print(f"El cuadrado de {i} es: {cuadrado}")

for num in range(1,61):
    cuadradonum = num * num
    print(f"El cuadrado de {num} es: {cuadradonum}")