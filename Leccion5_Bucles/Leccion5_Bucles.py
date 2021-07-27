# Leccion 5 - Bucles
# ------------------

# Bucles While
# No es necesario usar "else: ..." después del bucle

# Ejemplo 1 - Bucle infinito (si condicion = True)

condicion = False
while condicion:
    print("Ejecutando bucle While")
else:
    print("Fin de ciclo while")

# Ejemplo 2
N = 0
while N <= 10:
    print("N =", N)
    N += 1
else:
    print("Fin del ciclo While")   
    
print("--------------------------------------------")

# Bucles for
# No es necesario usar "else: ..." después del bucle

# Ejemplo 1
# Imprime en pantalla los numeros enteros desde "a" hasta "b - 1".
# En este caso imprime los valores 0, 1, 2, ..., 10 - 1
# a), b) y c) son equivalentes. 
a = 0
b = 5

# a)
for M in range(b): # Solo si empieza desde cero.
    print("M =", M)
else:
    print("Fin del ciclo for")

# b)
for M in range(a, b):
    print("M =", M)
else:
    print("Fin del ciclo for")

# c)
for M in range(a, b, 1):
    print("M =", M)
else:
    print("Fin del ciclo for")    


# Ejemplo 2
# Imprime los valores entre "a" y "b - 1" de dos en dos unidades.
for P in range(a, b, 2):
    print("P =", P)
    
# Ejemplo 3
# Imprime de uno en uno cada uno de los caracteres del string.
for i in "Computador":
    print(i)

print("--------------------------------------------")
    
# Palabras break y continue

# Ejemplo 1 - Break
# Imprime la primera vocal minuscula de la palabra.
cadena = "Manzana"
for i in cadena:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i)
        break       # Si se utiliza la palabra break, no se ejecuta el "else: ..."
else:
    print("Fin del ciclo for") # No se imprime
    
# Ejemplo 2 - Continue
# Imprime numeros pares entre 0 y 10
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)