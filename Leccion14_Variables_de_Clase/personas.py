class Persona:
    contador_personas = 0
    
    def __init__(self, nombre, edad):
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas