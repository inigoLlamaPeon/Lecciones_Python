# Leccion 9 - Encapsulamiento
# ---------------------------

# Evitar que accedamos a los atributos de 
# una clase de una manera directa

class Persona:
    def __init__(self, n):
        """El doble guion bajo indica que la variable es privada"""
        self.__nombre = n
        self.__edad = 18 # No hace falta declararlo en el init
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
        
p1 = Persona("Juan")
print("get_nombre:", p1.get_nombre())
p1.set_nombre("Ana")
print("set_nombre:", p1.get_nombre())
print("get_edad:", p1.get_edad())
p1.set_edad(21)
print("set_edad:", p1.get_edad())

# Metodos privados
class Persona2:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre                # Atributo publico
        self._ape_paterno = ape_paterno     # Atributo protegido
        self.__ape_materno = ape_materno    # Atributo privado
        
    """Definir metodo privado"""
    def __metodo_privado(self):
        print("Nombre:", self.nombre)
        print("Apellido paterno:", self._ape_paterno)
        print("Apellido paterno:", self.__ape_materno)
    
    def metodo_publico(self):
        self.__metodo_privado()

    def get_apeMat(self):
        return self.__ape_materno
    
    def set_apeMat(self, ape_materno):
        self.__ape_materno = ape_materno
        
p = Persona2("Juan", "Lopez", "Garcia")
# No permite el uso de -> p.__metodo_privado()
p.metodo_publico()
p._ape_paterno = "Dominquez"
print("p.nombre:", p.nombre)
print("p._ape_paterno:", p._ape_paterno)
p.metodo_publico()
print("get_apeMat():", p.get_apeMat())
p.set_apeMat("Perez")
print("set_apeMat():", p.get_apeMat())