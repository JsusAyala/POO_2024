import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='catalagomotosbd'  
    )
    
    cursor = conexion.cursor(buffered=True)
except Exception as e:
    print(f"Ocurrió un error al conectar con la base de datos: {e}")