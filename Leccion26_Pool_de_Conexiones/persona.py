from logger_base import log

class Persona:
    def __init__(self, id_persona = None, nombre = None, apellido = None, email = None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f''' Id Persona: {self._id_persona}, Nombre: {self._nombre}, Apellido: {self._apellido}, email: {self._email}'''

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == "__main__":
	# Crear objeto con todos los datos
    p1 = Persona(1, 'Juan', 'Perez', 'jperez@email.com')
    log.debug(p1)
    # Crear objeto sin id_persona especificado (Simular Insert)
    p2 = Persona(nombre = 'Pedro', apellido = 'Garcia', email = 'pgarcia@email.com')
    log.debug(p2)
    #Borrar datos de persona con id_persona = 1 (Simular Delete)
    p3 = Persona(id_persona = 1)
    log.debug(p3)