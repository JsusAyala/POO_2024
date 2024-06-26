"""
Sintanxis: 
lamba argumentos: expreciones


funciones lamba se puede convertir en funcion normales pero No viceversa 

"""
#Ejemplo 1
#def suma (n1,n2)
#   return n1 + n2 
#print (suma(4,2))


suma = lambda n1,n2: n1 +n2 
print (suma(4,3))


#ejemplo 2

elevar = lambda num: num + num
print(elevar(4))

#Ejemplo 3

def mensaje():
 nombre = input("Ingresa tu nombre: ")
 return f"Hola, {nombre}: Eres increible"
print (mensaje())






