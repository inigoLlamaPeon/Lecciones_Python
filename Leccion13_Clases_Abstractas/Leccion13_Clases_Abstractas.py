# Lección 13 - Clases Abstractas
# ------------------------------

# Una clase es abstracta cuando tiene uno o mas
# metodos declarados, pero no implementados.
# No se pueden crear objetos de una clase abstracta

from abc import ABC, abstractmethod
# ABC - Abstract Base Class
# abstract method - Decorador (agrega funcionalidad a nuestros metodos)

class FiguraGeometrica2:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    @abstractmethod
    def area(self):
        pass

class Color2:
    def __init__(self, color2):
        self.color2 = color2
    
class Cuadrado2(FiguraGeometrica2, Color2):
    def __init__(self, lado, color2):
        FiguraGeometrica2.__init__(self, lado, lado)
        Color2.__init__(self, color2)
    
    def area(self):
        return self.alto * self.ancho
    
cuadrado = Cuadrado2(2, "Negro")
print(cuadrado.area())
print(cuadrado.color2)