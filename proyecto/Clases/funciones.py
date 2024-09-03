from conexionBd1 import *
import os
class Moto:
    def __init__(self, id, marca, modelo, anio, precio, tipo, cilindrada, potencia, color, cantidadDisponible):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.color = color
        self.cantidadDisponible = cantidadDisponible

    def crear(self):
        try:
            sql="INSERT INTO moto VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valor=(self.marca, self.modelo, self.anio, self.precio, self.tipo, self.cilindrada, self.potencia, self.color, self.cantidadDisponible)
            cursor.execute(sql,valor)
            conexion.commit()
            print("Moto creada exitosamente")
            return True
        except Exception as e:
            print(f"Error al crear la Moto: {e}")
            return False    
    
    @staticmethod
    def mostrar():
        try:
            id=(input("Ingrese el id: "),)
            cursor.execute(
                "select * from moto where id=%s ",id
            )
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def actualizar():
        try:
            os.system
            id=input("Ingrese el id: ")
            marca=input("Ingrese la marca: ")
            modelo=input("Ingrese el modelo: ")
            anio=input("Ingrese el año: ") 
            precio=input("Ingrese el precio: ")
            tipo=input("Ingrese el tipo: ")
            cilindrada=input("Ingrese la cilindrada: ")
            potencia=input("Ingrese la potencia: ")
            color=input("Ingrese el color: ")
            cantidadDisponible=input("Ingrese la cantidad: ")
            sql="update moto set marca=%s,modelo=%s,anio=%s,precio=%s,tipo=%s,cilindrada=%s,potencia=%s,color=%s, cantidadDisponible=%s where id=%s"
            cursor.execute(sql,(marca, modelo, anio, precio, tipo, cilindrada, potencia, color, cantidadDisponible,id))
            conexion.commit()
            print("Se actualizo con exito")
            esperarTecla()
            os.system 
            return True
        except:
    
            return False
        



class cliente:
    def __init__(self, id, nombre, apellido, email, telefono, direccion):
        self.id = id 
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def crear(self):
        try:
            sql="INSERT INTO cliente VALUES (NULL, %s, %s, %s, %s, %s)"
            valor=(self.nombre, self.apellido, self.email, self.telefono, self.direccion)
            cursor.execute(sql,valor)
            conexion.commit()
            print("El cliente a sido creado exitosamente")
            return True
        except Exception as e:
            print(f"Error al crear el cliente: {e}")
            return False
          
    @staticmethod              
    def mostrar():
        try:
            id=(input("Ingrese el id del cliente: "),)
            cursor.execute(
                "select * from cliente where id=%s ",id
            )
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod       
    def actualizar():
        try:
            os.system
            id=input("Ingrese eo ID de cliente: ")
            nombre=input("ingrese su nombre: ") 
            apellido=input("Ingrese su apellido: ")
            email=input("Ingrese su  email: ")
            telefono=input("Ingrese su numero de telefono: ")
            direccion=input("ingrese su direccion: ")
            sql="update cliente set nombre=%s,apellido=%s,email=%s,telefono=%s,direccion=%s where id=%s"
            cursor.execute(sql,(nombre,apellido,email,telefono,direccion,id))
            conexion.commit()
            print("Se actualizo con exito")
            esperarTecla()
            os.system
            return True
        except:
    
            return False
        


class empleado:
    def __init__(self, id, nombre, apellido, email, telefono, puesto):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.puesto = puesto
        
    def crear(self):
        try:
            sql="INSERT INTO empleado VALUES (NULL, %s, %s, %s, %s, %s)"
            valor=(self.nombre, self.apellido, self.email, self.telefono,self.puesto )
            cursor.execute(sql,valor)
            conexion.commit()
            print("El empleado a sido creado exitosamente")
            return True
        except Exception as e:
            print(f"Error al crear al empleado: {e}")
            return False
          
    @staticmethod              
    def mostrar():
        try:
            id=(input("Ingrese el id del empleado: "),)
            cursor.execute(
                "select * from empleado where id=%s ",id
            )
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod       
    def actualizar():
        try:
            os.system
            id=input("Ingrese eo ID del empleado: ")
            nombre=input("ingrese su nombre: ") 
            apellido=input("Ingrese su apellido: ")
            email=input("Ingrese su  email: ")
            telefono=input("Ingrese su numero de telefono: ")
            puesto=input("ingrese su puesto: ")
            sql="update empleado set nombre=%s,apellido=%s,email=%s,telefono=%s,puesto=%s where id=%s"
            cursor.execute(sql,(nombre,apellido,email,telefono,puesto,id))
            conexion.commit()
            print("Se actualizo con exito")
            esperarTecla()
            os.system
            return True
        except:
    
            return False
        








class venta:
    def __init__(self, id, clienteid, empleadoid, fechaVenta, CostoDVenta):
        self.id = id
        self.clienteid = clienteid
        self.empleadoid = empleadoid
        self.fechaVenta = fechaVenta
        self.costoDVenta = CostoDVenta
  

    def crear(self):
        try:
            sql="INSERT INTO venta VALUES (NULL, %s, %s, %s, %s)"
            valor=(self.clienteid, self.empleadoid, self.fechaVenta, self.costoDVenta)
            cursor.execute(sql,valor)
            conexion.commit()
            print("La venta  sido creado exitosamente")
            return True
        except Exception as e:
            print(f"Error al generar la venta: {e}")
            return False
          
    @staticmethod              
    def mostrar():
        try:
            id=(input("Ingrese el id de la venta: "),)
            cursor.execute(
                "select * from venta where id=%s ",id
            )
            return cursor.fetchall()
        except:
            return []
        
    

class ticketventa:
    def __init__(self, id, ventaid, motoid, cantidad, preciototal):
        self.id = id
        self.ventaid = ventaid
        self.motoid = motoid
        self.cantidad = cantidad
        self.preciototal = preciototal
    
    def crear(self):
        try:
            sql="INSERT INTO ticketventa VALUES (NULL, %s, %s, %s, %s)"
            valor=(self.ventaid, self.motoid, self.cantidad, self.preciototal)
            cursor.execute(sql,valor)
            conexion.commit()
            print("El ticket a sido creado exitosamente")
            return True
        except Exception as e:
            print(f"Error al generar el ticket: {e}")
            return False
          
    @staticmethod              
    def mostrar():
        try:
            id=(input("Ingrese el id de la venta: "),)
            cursor.execute(
                "select * from ticketventa where id=%s ",id
            )
            return cursor.fetchall()
        except:
            return []    


def esperarTecla():
    input("Presiona cualquier tecla para continuar...")
    input()    






