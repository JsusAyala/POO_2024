from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="create table cliente (id int primary key auto_increment, nombre varchar(60),direccion varchar(120),tel varchar(10))"

    micursor.execute(sql)
except:
    print(f"Ocurrio un error por favor vuelva a intentarlo mas tarde")
else:
    print("Se creo la tabla exitosamente")