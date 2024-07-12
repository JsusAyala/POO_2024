from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="INSERT INTO `clientes`(`id`, `nombre`, `direccion`, `tel`) VALUES ('NULL','Juan Polainas','Col. del valle','6181234567')"
    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el sql
    conexion.commit()
except:
    print("Ocurrio un error por favor vuelva a intentarlo mas tarde")
else:
    print("Se inserto la tabla con exito")