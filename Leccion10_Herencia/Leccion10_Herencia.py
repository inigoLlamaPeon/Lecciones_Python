# Lección 10 - Herencias
# ----------------------

# Clase padre -> Persona (nombre, edad)
# Clase hija -> Empleado (caracteristicas de persona mas sueldo)

from Leccion9_Encapsulamiento import Persona2


class Persona: # Se puede declarar de la forma "class Persona (object):"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "Nombre:" + self.nombre + ", Edad:" + str(self.edad)

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def __str__(self):
        return super().__str__() + ", Sueldo:" + str(self.sueldo)
    
persona = Persona("Juan", 28)
print(persona)

persona2 = Empleado("Carlos", 28, 10000)
print(persona2)

persona2.nombre = "Maria"
persona2.sueldo =  20000
print(persona2)