#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
limite=int(num2-1)
while num1 in range(num1,limite):
    num1+=1
    if num1 % 2 != 0:
        print(num1)