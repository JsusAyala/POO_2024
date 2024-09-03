from Motos_ReporteParcial import *

opcion=True
while opcion:
    print("\n\t..::: MOTOS :::... \n..::: Sistema de Gestion de Motos:::...\n 1.- Motocicletas \n 2.- Cuatrimotos \n 3.- Deportivas \n 4.- Ayuda \n 5.- Salir ")
    opcion=input("\t Elige una opción: ").upper()

    if opcion=="1" or opcion=="MOTOCICLETAS":
        print("Motocicleta 1")
        motocicleta1=Motos("Gris","Italika","150Z",90,14,100,29999)
        motocicleta1.getInfo()
        
        print("Motocicleta 2")
        motocicleta2=Motos("Negro","HERO","HUNK 160",105,15,100,41999)
        motocicleta2.getInfo()

    elif opcion=="2" or opcion=="CUATRIMOTOS":
        print("Cuatrimoto 1")
        cuatrimoto1=ATV("Verde con Negro","Italika","ATV180",65,9.38,150,42999,"Automatica por cadena",1)
        cuatrimoto1.getInfo()

        print("Cuatrimoto 2")
        cuatrimoto2=ATV("Negro","Italika","ATV250",150,14.8,220,74999,"Semiautomatica",1.2)
        cuatrimoto2.getInfo()

    elif opcion=="3" or opcion=="DEPORTIVAS":
        print("Moto Deportiva 1")
        moto1=Deportivas("Blanca","BAJAJ","PULSAR RS 200 CC 2024",120,23.5,130,75499,"Estandar",6)
        moto1.getInfo()

        print("Moto Deportiva 2")
        moto2=Deportivas("Naranja","KTM","RC200",180,26,120,89999,"Estandar",6)
        moto2.getInfo()

    elif opcion=="4" or opcion=="AYUDA":
        print("En caso de requerir ayuda\nLlame al siguiente numero\n 555-123-45-67 ")

    elif opcion=="5" or opcion=="SALIR":
        print("Gracias por su visita, vuelva pronto...")
        opcion=False
    
    else:
        print("Opcion invalida \n Favor ingresar una opcion valida")
        espereTecla()
