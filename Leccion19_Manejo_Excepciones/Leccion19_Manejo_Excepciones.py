# Lección 19 - Manejo de Excepciones
# ----------------------------------

# El orden de las excepciones debe ser
# mas a menos especifica

# La variable res se usa unicamente dentro
# del bloque try-except

# Se ejecuta el bloque else cuando no hay
# ninguna excepcion

# El bloque finally se ejcuta siempre

from numerosIdenticos import numerosIdenticos as nI

#a = 0
#b = 5

#a = 0
#b = 's'

a = 5
b = 5
try:
    # res = b / a  # ZDE
    # res = 1000.5**2000.8 # AE
    if a == b:
        raise nI("Numeros Identicos")
        #raise ValueError("Error de Valor")
    res = a / b
# except Exception as e:
#    print(f'Ocurrio un error:', {e}, type(e))
except ZeroDivisionError as zde:
    print(f'Ocurrio un error:', {zde}, type(zde))
except ArithmeticError as ae:
    print(f'Ocurrio un error:', {ae}, type(ae))
except Exception as e:
    print(f'Ocurrio un error:', {e}, type(e))
else:
    print("No hay una excepcion")
finally:
    print("Ejecución finalizada")

print("Continuamos...")
