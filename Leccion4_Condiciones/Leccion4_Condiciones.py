# Condiciones if, else y elif
# ---------------------------

# Ejemplo  If / Else
# Los 2 codigos son equivalentes

# a)
condicion = True
if condicion == True:
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")

# b)
if condicion:
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")   
    
    
# Ejemplo 2 - If / Else If / Else

N = 9
if N == 1:
    print("El numero 1")
elif N == 2:
    print("El numero es 2")
elif N == 3:
    print("El numero es 3")
else:
    print("N no es ninguno de los numeros anteriores")
    
# Ejemplo 3 - Operador Ternario

# Si se cumple la condicion "not(M % 2 == 0)", ejecuta
# la orden situada a la izquierda del "if". En caso de
# no cumplirla ejecuta la sentencia que esta a la
# derecha del "else".

M = 9
print("Es numero impar") if not(M % 2 == 0) else print("No es impar")

if not(M % 2 == 0):
    print("Es numero impar")
else: 
    print("No es impar")
    
# Ejemplo 4 - If / Else anidados

P = 25

if P >= 10:
    if P > 30:
        print("El numero es mayor que 30")
    elif P > 20:
        print("El numero es mayor que 20")
    elif P > 15:
        print("El numero es mayor que 15")
    else:
        print("El numero es mayor o igual a 10")
else:
    print("El numero es menor que 10")
    
# Ejemplo 5 If / else con multiples condiciones

Q = 15

if Q >= 10 and Q <= 20:
    print("El numero esta dentro del rango")
else:
    print("El numero esta fuera del rango")

if Q < 10 or Q > 20:
    print("El numero esta fuera del rango")
else:
    print("El numero esta dentro del rango")