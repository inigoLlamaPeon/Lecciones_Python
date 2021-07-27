# Leccion 11 - Modulos
# --------------------

import biblioteca as bib                  # Modulo en la misma carpeta
from moduloAux import biblioteca2 as bib2 # Modulo en distinta carpeta
#import moduloAux.biblioteca2 as bib2     # Equivalente
from moduloAux.biblioteca2 import Persona # Las clases se importan de forma independiente

print("Suma:", bib.sumar(2, 3))
print("Resta:", bib.resta(3, 1))
print("Producto:", bib.producto(10, 5))
print("Division:", bib.division(10.0, 3.4))
print("Potencia:", bib2.potencia(2, 5))

p1 = Persona("Juan", 25)
print(p1)