#Concatenar cadenas de caracteres con contenido de variables

nombre="Jesus Ayala"
especialidad="Area de Desarrollo de SW Multiplataforma"
carrera="Ingeniero en Gestion y Desarrollo de SW"

#1er forma de concatenar
print("Mi nombre es: "+nombre+" Estoy en la +especialidad de: "+especialidad+" en la carrera de: "+carrera)

print("\n")

#2da forma de concatenar
print("Mi nombre es: ",nombre," Estoy en la +especialidad de: ",especialidad," en la carrera de: ",carrera)

print("\n")

#3ra forma de concatenar
print(f"Mi nombre es: {nombre} Estoy en la +especialidad de: {especialidad} en la carrera de: {carrera}")

print("\n")

#4ta forma de concatenar
print("Mi nombre es:{} Estoy en la +especialidad de: {}, en la carrera de: {}". format(nombre,especialidad,carrera))

print("\n")

#5to forma de concatenar
print('Mi nombre es: '+nombre+' Estoy en la +especialidad de: '+especialidad+' en la carrera de: '+carrera)

print("\n")