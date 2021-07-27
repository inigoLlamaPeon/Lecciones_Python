

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color:" + self.color + ", Ruedas:" + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__() + ", Velocidad:" + str(self.velocidad)
        

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ", Tipo:" + str(self.tipo)
    
coche = Coche("Rojo", 4, 120)
print(coche)

bicicleta = Bicicleta("Negro", 2, "Urbana")
print(bicicleta)