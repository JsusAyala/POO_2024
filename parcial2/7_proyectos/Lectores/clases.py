class lectores:
    def __init__(self,nombre,direccion,telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
    
    def reservar(self):
        print("Esta reservado este libro")

    def entregar(self):
        print("Esta entregado este libro")

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self,direccion):
        self.direccion=direccion
    
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self,telefono):
        self.telefono=telefono

class estudiantes(lectores):
    def __init__(self, nombre, direccion, telefono,carrera,matricula):
        super().__init__(nombre, direccion, telefono)
        self.carrera=carrera
        self.matricula=matricula
    
    def reservar(self):
        print(f"El estudiante: {self.getNombre()} reservo un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

    def entregar(self):
        print(f"El estudiante: {self.getNombre()} entrego un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

    def getCarrera(self):
        return self.carrera
    
    def setCarrera(self,carrera):
        self.carrera=carrera
    
    def getMatricula(self):
        return self.matricula
    
    def setMatricula(self,matricula):
        self.matricula=matricula
    
class docentes(lectores):
    def __init__(self, nombre, direccion, telefono,modalidad,num_empleado):
        super().__init__(nombre, direccion, telefono)
        self.modalidad=modalidad
        self.num_empleado=num_empleado
    
    def reservar(self):
        print(f"El docente: {self.getNombre()} reservo un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

    def entregar(self):
        print(f"El docente: {self.getNombre()} entrego un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

    
    def getModalidad(self):
        return self.modalidad
    
    def setModalidad(self,modalidad):
        self.modalidad=modalidad
    
    def getNum_empleado(self):
        return self.num_empleado
    
    def setNum_empleado(self,num_empleado):
        self.num_empleado=num_empleado