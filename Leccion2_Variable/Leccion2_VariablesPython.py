# Variables en Python
# -------------------

# Variables numéricas
x = 3       # Tipo entero (x = 3.0 sería tipo float)
y = 5.2     # Tipo float
z = x + y   # Tipo float
print("z = x + y =", z)
print("Tipo de variable x : ", type(x))
print("Tipo de variable y : ", type(y))
print("Tipo de variable z : ", type(z))

# Las variables x, y, z apuntan a una dirección de
# memoria donde están almacenados los valores.
# En el caso de tener una variable w = z,
# la dirección a la que apuntan tanto w como z
# es la misma.

# La función id() indica la dirección de memoria. 
print("Direccion de memoria de x : ", id(x))

# Strings / Cadenas
a = "H"   
b = "Hola "
c = "Mundo"
print("b + c = ", b + c) # Concatenacion de strings

# Variables Booleanas (siempre 1ª letra mayúscula)
t = True
f = False
print("t = ", t)
print("f = ", f)
m = 5
n = 2
resultado = m < n
print("m < n :", resultado)
print("Tipo de variable resultado : ", type(resultado))