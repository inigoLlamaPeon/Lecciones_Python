# Lección 16 - Sobrecarga de Operadores
# -------------------------------------

from persona import Persona
# Operador Suma
a = 2
b = 3
print("a + b = ", a + b)

A = "Hola"
B = " Mundo"
print("A + B = ", A + B)

x = [1, 2, 3]
y = [4, 5, 6]
print("x + y = ", x + y)

# Definimos las operaciones dentro de la clase Persona
persona1 = Persona("Juan", 20)
persona2 = Persona("Carlos", 17)
print(persona1 + persona2)
print(persona1 - persona2)
