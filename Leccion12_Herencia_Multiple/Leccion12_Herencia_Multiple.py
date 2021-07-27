# Leccion 12 - Herencia Multiple
# ------------------------------

from cuadrado import Cuadrado

square = Cuadrado(5, "Azul")
print(square.area())
print(square.color)

# Method Resolution Order
print(Cuadrado.mro())