import mysql.connector

try:
    #Conexion con la BD de MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )
except Exception as e:
 print(f"Ocurrio un error por favor vuelva a intentarlo mas tarde")
