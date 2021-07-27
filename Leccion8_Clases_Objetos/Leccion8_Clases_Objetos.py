# Leccion 8 - Clases y Objetos
# ----------------------------

# Clases: Es una plantilla a partir de la cual se
# pueden crear objetos. Se componen de atributos
# y metodos

# Por convencion, la primera letra de cada palabra
# se escribe con mayuscula.

class Persona:
    # Definimos metodo __init__()
    def __init__(self, nombre, edad):
        self.nombre = nombre    # self hace referencia al objeto de la clase
        self.edad = edad

# Crea objeto de manera automatica (la clase es un objeto en si mismo)
Persona.nombre = "Juan"
Persona.edad = 28
print("Nombre:", Persona.nombre)
print("Edad:", Persona.edad)
print("Direccion de Memoria:", id(Persona))

# Creacion de un objeto
humano1 = Persona("Miguel", 30)
print("Nombre:", humano1.nombre)
print("Edad:", humano1.edad)
print("Direccion de Memoria:", id(humano1))

humano2 = Persona("Maria", 23)
print("Nombre:", humano2.nombre)
print("Edad:", humano2.edad)
print("Direccion de Memoria:", id(humano2))


# Clase con atributos y metodos

class Aritmetica:
    """Clase artimetica para realizar operaciones aritmeticas"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self): # Se usa self para acceder a los atributos de la clase
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def producto(self):
        return self.operando1 * self.operando2
    
    def potencia(self):
        return self.operando1 ** self.operando2

arit = Aritmetica(4, 3)
print("Resultado de la suma:", arit.sumar())
print("Resultado de la resta:", arit.restar())
print("Resultado del producto:", arit.producto())
print("Resultado de la potencia:", arit.potencia())

# Clase con "this"
class Persona2:
    # El asterisco simple indica que es opcional
    # El asterisco doble indica que es un diccionario
    def __init__(this, nombre, edad, *tupla, **diccionario):
        this.N = nombre
        this.E = edad
        this.T = tupla
        this.D = diccionario
        
    def desplegar(this):
        print("Nombre:", this.N)
        print("Edad:", this.E) 
        print("Tupla:", this.T)
        print("Diccionario:", this.D)
        
p1 = Persona2("Ana", 95, 2, "doce", [2, 3], (5, 7), m = "mango", p = "pera", l = "lima")
print("Nombre:", p1.N)
print("Edad:", p1.E)
print("Tupla:", p1.T)
print("Tipo p1.T", type(p1.T))
print("Tipo T[0]", type(p1.T[0]))
print("Tipo T[1]", type(p1.T[1]))
print("Tipo T[2]", type(p1.T[2]))
print("Tipo T[3]", type(p1.T[3]))
print("Diccionario:", p1.D)
p1.desplegar()
