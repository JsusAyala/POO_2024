from conexionBd import *
import os
import hashlib
import datetime

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
        
    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from cliente where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False

class Auto:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif

    def crear(self):
        try:
            sql = "INSERT INTO autos VALUES (NULL, %s, %s, %s, %s, %s)"
            valor = (self.matricula, self.marca, self.modelo, self.color, self.nif)
            cursor.execute(sql, valor)
            conexion.commit()
            print("El auto ha sido creado exitosamente")
            return True
        except Exception as e:
            print(f"Error al crear el auto: {e}")
            return False

    @staticmethod
    def mostrar():
        try:
            matricula = (input("Ingrese la matrícula del auto: "),)
            cursor.execute("SELECT * FROM autos WHERE matricula=%s", matricula)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar el auto: {e}")
            return []

    @staticmethod
    def actualizar():
        try:
            matricula = input("Ingrese la matrícula del auto: ")
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            color = input("Ingrese el color: ")
            nif = input("Ingrese el NIF: ")
            sql = "UPDATE autos SET marca=%s, modelo=%s, color=%s, nif=%s WHERE matricula=%s"
            cursor.execute(sql, (marca, modelo, color, nif, matricula))
            conexion.commit()
            print("El auto se ha actualizado con éxito")
            return True
        except Exception as e:
            print(f"Error al actualizar el auto: {e}")
            return False

    @staticmethod
    def eliminar(matricula):
        try:
            cursor.execute("DELETE FROM autos WHERE matricula=%s", (matricula,))
            conexion.commit()
            print("El auto ha sido eliminado con éxito")
            return True
        except Exception as e:
            print(f"Error al eliminar el auto: {e}")
            return False
        
class Revisiones:
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofreno, otros, matricula):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofreno = cambiofreno
        self.otros = otros
        self.matricula = matricula

    def crear(self):
        try:
            sql = "INSERT INTO revisiones VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            valor = (self.cambiofiltro, self.cambioaceite, self.cambiofreno, self.otros, self.matricula)
            cursor.execute(sql, valor)
            conexion.commit()
            print("La revisión ha sido creada exitosamente")
            return True
        except Exception as e:
            print(f"Error al crear la revisión: {e}")
            return False

    @staticmethod
    def mostrar():
        try:
            no_revision = (input("Ingrese el número de revisión: "),)
            cursor.execute(
                "SELECT * FROM revisiones WHERE no_revision=%s", no_revision
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar la revisión: {e}")
            return []

    @staticmethod
    def actualizar():
        try:
            no_revision = input("Ingrese el número de revisión: ")
            cambiofiltro = input("Ingrese si hubo cambio de filtro (Sí/No): ")
            cambioaceite = input("Ingrese si hubo cambio de aceite (Sí/No): ")
            cambiofreno = input("Ingrese si hubo cambio de freno (Sí/No): ")
            otros = input("Ingrese otros cambios realizados: ")
            matricula = input("Ingrese la matrícula del vehículo: ")
            sql = "UPDATE revisiones SET cambiofiltro=%s, cambioaceite=%s, cambiofreno=%s, otros=%s, matricula=%s WHERE no_revision=%s"
            cursor.execute(sql, (cambiofiltro, cambioaceite, cambiofreno, otros, matricula, no_revision))
            conexion.commit()
            print("La revisión ha sido actualizada exitosamente")
            return True
        except Exception as e:
            print(f"Error al actualizar la revisión: {e}")
            return False

    @staticmethod
    def eliminar(no_revision):
        try:
            cursor.execute(
                "DELETE FROM revisiones WHERE no_revision=%s",
                (no_revision,)
            )
            conexion.commit()
            print("La revisión ha sido eliminada exitosamente")
            return True
        except Exception as e:
            print(f"Error al eliminar la revisión: {e}")
            return False

def esperarTecla():
  print("\n \t \tDa click en cualquier tecla para continuar ...")
  input() 

def borrarPantalla():
  import os  
  os.system("cls")

class Usuario:
    def __init__(self, nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos=apellidos
        self.email=email
        self.contrasena = self.hash_password(password)

    def hash_password(self,contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar(self):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                (self.nombre,self.apellidos,self.email,self.contrasena,fecha)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
          return None         
        
