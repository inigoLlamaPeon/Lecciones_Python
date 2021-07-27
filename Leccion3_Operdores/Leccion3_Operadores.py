# Operadores en Python
# --------------------

# Operadores Aritméticos

# Suma
a = 3
b = 2
suma = a + b
print("Suma = ", suma)

# Resta
resta = a - b
print("Resta = ", resta)

# Multiplicación
multi = a * b
print("Multiplicacion =", multi)

# División
div = a / b
print("Division =", div)

# Módulo (Resto de la operación a / b)
mod = a % b
print("Modulo =", mod)

# Potencia
pot = a ** b
print("Potencia =", pot)

# ------------------------------------------------------

# Operadores de asignación

x = 2
print("x =", x)

# x = x + 3
x += 3       
print("x += 3 ->", x)

# x = x - 3
x -= 3       
print("x -= 3 ->", x)

# x = x * 5
x *= 5       
print("x *= 5 ->", x)

# x = x / 3
x /= 3
print("x /= 3 ->", x)

# x = x % 2
x %= 2
print("x %= 2 ->", x)

# ------------------------------------------------------

# Operadores de Comparación

a = 5
b = 10

# Igualdad
resultado = (a == b)    # No hacen falta los paréntesis 
print("a == b ->", resultado)

# Diferencia
resultado = a != b
print("a != b ->", resultado)

# Mayor
resultado = a > b
print("a > b ->", resultado)

# Menor
resultado = a < b
print("a < b ->", resultado)

# Mayor o igual
resultado = a >= b
print("a >= b ->", resultado)

# Menor o igual
resultado = a <= b
print("a <= b ->", resultado)

# Ejemplo: Es par?
a = 5
if(a % 2 == 0):
    print("Numero par")
else: 
    print("Numero impar")
    
# Ejemplo: Mayor de edad?
a = 25
if a >= 18:
    print("Es un adulto")
else:
    print("Es menor de edad")

# ------------------------------------------------------
   
# Operadores Lógicos

# AND

# Variable dentro de un rango
a = 3
minimo = 0
maximo = 5
resultado = a >= minimo and a <= maximo
print("Variable dentro del rango ->", resultado)

# OR

vacaciones = False
descanso = True
# Python interpreta
# if vacaciones == True or descanso == True:

if vacaciones or descanso:
    print("Puedes ir al parque")
else:
    print("No puedes ir al parque")
    
# NOT

vacaciones = False
descanso = False
if not(vacaciones or descanso):
    print("No puedes ir al parque")
else:
    print("Puedes ir al parque")

# ------------------------------------------------------

# Operadores a nivel de bit

# Desplazamiento de bits a la derecha
# Cada posición desplazada equivale a multiplicar por dos
a = 7
print("a << 2 =", a << 2)

# Desplazamiento de bits a la derecha
# Cada posición desplazada equivale a dividir entre 2
b = 15
print("b >> 1 =", b >> 1)

# Para la siguiente parte las variables serán números representados en binario
# Para indicar que el numero se encuentra en formato binario se coloca "0b" delante

# Operador | (or a nivel de bit)

# bit a | bit b | resultado
#   0   |   0   |    0
#   1   |   0   |    1
#   0   |   1   |    0
#   1   |   1   |    1

c = 0b1100
d = c | 0b0011
print("d = c | 0b0011 ->", bin(d)) # bin() -> Representa numero en formato binario

# Operador & (and a nivel de bit)

# bit a | bit b | resultado
#   0   |   0   |    0
#   1   |   0   |    0
#   0   |   1   |    0
#   1   |   1   |    1

e = 0b1100
f = e & 0b1011
print("f = e & 0b1011 ->", bin(f))

# Operador ~ (not a nivel de bit)

# Al aplicar el operador ~ los bits que son 1 pasan a ser 0 y viceversa
# En el caso de Python ocurre algo distinto. La operación que hace es:
# ~variable = - variable - 1
g = 0b1100
print("~g ->", bin(~g))
h = 40
print("~h = ", ~h)
i = 27
print("~i = ", ~i)

# Operador ^ (xor)

# bit a | bit b | resultado
#   0   |   0   |    0
#   1   |   0   |    1
#   0   |   1   |    1
#   1   |   1   |    0

x = 0b0101
y = 0b0011
z = x ^ y
print("x ^ y =", bin(z))