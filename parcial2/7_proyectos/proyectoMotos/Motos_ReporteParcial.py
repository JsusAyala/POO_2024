
class Motos:
    def __init__(self,color,marca,modelo,velocidad,caballaje,pesoMax,precio):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.pesoMax=pesoMax
        self.precio=precio

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPesoMax(self):
       return self.pesoMax

    def setPesoMax(self,pesoMax):
      self.pesoMax=pesoMax 

    def getPrecio(self):
       return self.precio

    def setPesoMax(self,precio):
      self.precio=precio 

    def getInfo(self):
       print(f"Marca: {self.getMarca()} {self.getColor()}\nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp \nCon una capacidad maxima de peso de {self.getPesoMax()}Kg\n Tiene un precio de {self.getPrecio()} pesos mexicanos.")  

class ATV(Motos):
   def __init__(self,color,marca,modelo,velocidad,caballaje,pesoMax,precio,transmision,capacidadCarga):
    super().__init__(color,marca,modelo,velocidad,caballaje,pesoMax,precio)
    self.transmision=transmision
    self.capacidadCarga=capacidadCarga

   CC=""

   def clindrada(self,CC):
    self.CC=CC
    return self.CC

   def getTransmision(self):
     return self.transmision

   def setTransmision(self,transmision):
      self.transmision=transmision  

   def getcapacidadCarga(self):
     return self.capacidadCarga

   def setcapacidadCarga(self,capacidadCarga):
      self.capacidadCarga=capacidadCarga 

   def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}\nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h, una potencia de {self.getCaballaje()} hp, con una transmision {self.getTransmision()}\nCon una capacidad maxima de peso de {self.getPesoMax()}Kg  y una capacidad de carga de {self.getcapacidadCarga()} metro cubico\n Tiene un precio de {self.getPrecio()} pesos mexicanos.")       

class Deportivas(Motos):
  def __init__(self,color,marca,modelo,velocidad,caballaje,pesoMax,precio,transmision,velociades):
    super().__init__(color,marca,modelo,velocidad,caballaje,pesoMax,precio)
    self.transmision=transmision
    self.velocidades=velociades

  RPM=0
  def potencia(self,RPM):
      self.RPM=RPM
      return self.RPM

  def getTransmision(self):
     return self.transmision

  def setTransmision(self,transmision):
      self.transmision=transmision

  def getVelocidades(self):
    return self.velocidades

  def setVelocidades(self,velocidades):
    self.velocidades=velocidades

  def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}\nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h, una potencia de {self.getCaballaje()} hp, con una transmision {self.getTransmision()}\nCon una capacidad maxima de peso de {self.getPesoMax()}Kg y con {self.getVelocidades()} cambios de velocidades\n Tiene un precio de {self.getPrecio()} pesos mexicanos.")  

def espereTecla():
    print("Oprima cualquier tecla para continuar")    
    input()    


