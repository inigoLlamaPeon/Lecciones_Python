# Lección 15 - Diseño de Clases
# -----------------------------

from producto import Producto
from orden import Orden

p1 = Producto("Camisa", 150.0)
p2 = Producto("Pantalon", 100.0)
p3 = Producto("Zapatos", 300)
p4 = Producto("Calcetines", 50.0)
p5 = Producto("Corbata", 200.0)
productos1 = [p1, p2, p3]
productos2 = [p4, p5]
orden1 = Orden(productos1)
print(orden1)
print("Total:", orden1.calcular_total())
orden2 = Orden(productos2)
print(orden2)
print("Total:", orden2.calcular_total())

