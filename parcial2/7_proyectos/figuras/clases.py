class Figuras:
    def Area(self):
        print(self)
    
class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return (3.1416)*(self.radio**2)
    
class Rectangulo(Figuras):
    def __init__(self, largo, ancho):
        self.largo=largo
        self.ancho=ancho

    def area(self):
        return (self.ancho)*(self.largo)
    
class Triangulo(Figuras):
    def __init__(self, altura, ancho):
        self.altura=altura
        self.ancho=ancho

    def area(self):
        return ((self.ancho)*(self.altura))/2