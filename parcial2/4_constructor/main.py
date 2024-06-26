

from coches import *

print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)

coche1.getInfo()


print("Objeto 2")
coche2=("Azul","Nissan","2020",180,150,6)

coche2.getInfo()

#Implementar el encapsulamiento o visivilidad

print(coche1.atributo_publico)
#print(coche1.atributo_privado) NO ES POSIBLE
print(coche1.Metodopublico())
#coche1.Metodoprivado() NO ES POSIBLE
coche1.getMetodoPublico()



