# Insertar datos desde el terminal
# --------------------------------

print("Escriba algo en el terminal")
leido = input();
print("Enviado por terminal :", leido)

# Por defecto todo lo que se recibe desde el terminal,
# Python lo interpreta como si fuera una cadena.

# En el siguiente ejemplo, si m = 5 y n = 4, el resultado
# de la suma es la cadena "54".
m = input("Inserte un número :")
n = input("Inserte otro numero :")
print("m + n =", m + n)

# Para que python lo interprete como un numero, debe utilizar
# el comando int(input(...)) si se trata de un numero entero y
# float(input(...)) si se trata de un numero con punto flotante.
m = float(input("Inserte un número :"))
n = int(input("Inserte otro numero :"))
print("m + n =", m + n)