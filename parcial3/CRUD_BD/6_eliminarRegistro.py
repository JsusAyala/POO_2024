from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="delete from clientes where id=1"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el sql
    conexion.commit()

except:
    print("Ocurrio un error por favor vuelva a intentarlo mas tarde")
else:
    print("Se elimino la tabla con exito")