from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="select * from clientes"

    micursor.execute(sql)

    resultado=micursor.fetchall()

    for fila in resultado:
        print(f"Id:{fila[0]} | Nombre:{fila[1]}")

except:
    print("Ocurrio un error por favor vuelva a intentarlo mas tarde")
else:
    print("Se selecciono la tabla con exito")