conta_pres_parcial=0
med_sis_total=0
med_dia_total=0
pacientes=0

while True:
    pacientes+=1
    nombre=input("Nombre del paciente: ")
    sangre=input("Tipo de sangre del paciente: ")
    while True:
        conta_pres_parcial+=1
        med_sis=float(input("Ingrese la medicion de presion arterial SIStolica: "))
        med_sis_total+=med_sis
        med_dia=float(input("Ingrese la medicion de presion arterial DIAstolica: "))
        med_dia_total+=med_dia
        res_med_pres=input("Desea volver a realizar una medicion?(Si/No) ")
        if res_med_pres=="No":
            break
    pres_sis_promedio=med_sis_total/conta_pres_parcial
    print(f"El promedio de las mediciones de presion arterial SIStolica es de {pres_sis_promedio}")
    pres_dia_promedio=med_dia_total/conta_pres_parcial
    print(f"El promedio de las mediciones de presion arterial DIAstolica es de {pres_dia_promedio}")
    print("Para finalizar se realizara una medicion final")
    med_sis_final=float(input("Ingrese la medicion final de presion arterial SIStolica: "))
    med_dia_final=float(input("Ingrese la medicion final de presion arterial DIAstolica: "))
    pres_dia_final=(pres_dia_promedio+med_dia_final)/2
    pres_sis_final=(pres_sis_promedio+med_sis_final)/2
    print(f"La presion final arterial SIStolica es de {pres_sis_final}")
    print(f"La presion final arterial DIAstolica es de {pres_dia_final}")
    if pres_dia_final <= 80 and pres_sis_final <= 120:
        print("Tiene una presion artereial normal")
    res_pacientes=input("Deasea realizar la medicion de otro paciente?(Si/No) ")
    if res_pacientes=="No":
        break
print(f"El numero total de pacientes atendidos el dia de Hoy fue de {pacientes}")