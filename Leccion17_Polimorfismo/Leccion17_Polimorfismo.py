# Leccion 17 - Polimorfismo
# -------------------------

class Gerente:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Nombre y sueldo del gerente: {self.nombre}, {self.sueldo}'


class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Nombre y sueldo del empleado: {self.nombre}, {self.sueldo}'


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))


def imprimir_isinstance(objeto):
    print(type(objeto))
    if isinstance(objeto, Empleado):
        print(objeto.nombre)


gerente = Gerente("Juan Garcia", "3000")
empleado = Empleado("Jose Martinez", "1000")
print("print(gerente). ", gerente)
print("***************")
print("imprimir_detalles")
imprimir_detalles(gerente)
print("***************")
print("print(empleador): ", empleado)
print("***************")
print("imprimir_detalles")
imprimir_detalles(empleado)
print("***************")
print("imprimir_isinstance: ")
imprimir_isinstance(empleado)
