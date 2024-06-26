
energia_usada=float(input("Ingrese la cantidad de energia que se utilizo durante el mes: "))
if energia_usada >= 151:
    energia_usada_basica=150
    energia_usada_intermedio=energia_usada-energia_usada_basica
else:
    energia_usada_intermedio=0
energia_usada_basica=energia_usada-energia_usada_intermedio
pago_basico=energia_usada_basica*0.987
pago_intermedio=energia_usada_intermedio*1.203
pago_total=pago_intermedio+pago_basico
iva=pago_total*0.16
pago_final=pago_total+iva+12.56
print(f"El total a pagar es de {pago_final}, por el consumo de {energia_usada} kWh.")