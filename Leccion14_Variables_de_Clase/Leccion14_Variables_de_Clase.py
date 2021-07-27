# Leccion 14 - Variables de clase 
# -------------------------------

class MiClase:
    # Variable asociada a la clase y no al objeto
    variable_clase = "Mi variable de clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
# Para acceder a una variable de clase, no hace falta declarar un objeto
print("Variable de clase: ", MiClase.variable_clase)
objeto = MiClase("Variable instancia")
print ("Variable de clase: ", objeto.variable_clase)
print ("Variable de objeto:", objeto.variable_instancia)
objeto.variable_instancia = "Variable Instancia Modificada"
print("variable_intancia modificada: ", objeto.variable_instancia)
# Si se cambia Miclase.variable_clase por otro valor
# la variable_clase no cambia en los objetos creados antes del cambio.


# Variables de clase al vuelo
# Añadir nueva variable a una clase ya creada
MiClase.variable_clase2 = "Variable de clase 2"
print("Variable de clase 2 del objeto:", objeto.variable_clase2)

# Métodos Estáticos y de Clase
class MiClaseA:
    # Variable asociada a la clase y no al objeto
    variable_claseA = "Mi variable de clase A"
    
    def __init__(self, variable_instanciaA):
        self.variable_instanciaA = variable_instanciaA
    
    # La variable self hace referencia a objetos, por lo que
    # un metodo estatico no puede utilizarla
    @staticmethod
    def metodo_estatico():
        print("Metodo Estatico: ", MiClaseA.variable_claseA)
        
    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase: ", cls.variable_claseA)
    
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print("Variable de clase A: ", self.variable_claseA)
        print("Variable de Instancia A: ", self.variable_instanciaA)
        
        
MiClaseA.metodo_estatico()
MiClaseA.metodo_clase()

# Contexto Estático y Dinámico

objeto3 = MiClaseA("Variable de Instancia A")
objeto3.metodo_estatico()
objeto3.metodo_clase()
objeto3.metodo_instancia()

# Constantes en Python
# Se utilizan en un módulo separado
# Se pueden modificar pero no se aconseja

from constantes import MI_CONSTANTE
a = MI_CONSTANTE
# MI_CONSTANTE = "Valor de mi constantes" 
print("MI_CONSTANTE: ", a)

# Para importar todo
# from constantes import *
from constantes import Matematicas as Mates
print("PI: ", Mates.PI)

# Contador de Personas
from personas import Persona

persona1 = Persona('Juan', 28)
print(persona1)
persona2 = Persona('Karla', 30)
print(persona2)
persona3 = Persona('Eduardo', 25)
print(persona3)
print(f'Valor contador personas: {Persona.contador_personas}')

Persona.generar_siguiente_valor()
persona4 = Persona('Maria', 35)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')