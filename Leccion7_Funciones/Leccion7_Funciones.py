# Leccion 7 - Funciones y Metodos
# -------------------------------

# Funcion sin argumentos de entrada
def mi_funcion():
    print("Ejecutando funcion")
    
# Funcion con argumento de entrada
def funcion_arg(x):
    print("El argumento de entrada es:", x)

# Funcion con que comprueba la existencia 
# de un argumento
def funcion_arg_2(x = None):
    if x is None:
        print("No hay argumento de entrada")
    else:
        print("El argumento de entrada es:", x)

# Funcion con varios argumentos de entrada
def funcion_multiple(nombre, apellido):
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    
# Funcion con return y numero
# Si no se introduce ninguna variable de entrada
# los valores  por defecto son a = 0 y b = 0
def operacion(a = 0, b = 0):
    return a * b + 5

def op2(a = None, b = None):
    if a is None:
        a = 0
    if b is None:
        b = 0
    return a * b + 2

# Funcion con lista
def fun_lista(lista, nombre):
    lista.append(nombre)

# Funcion que concatena lista
def fun_list2(listaA, listaB):
    listaA.extend(listaB)

# Ejecucion de las funciones
mi_funcion()
funcion_arg("Funcion")
funcion_arg_2("Hola Mundo")
funcion_arg_2()
funcion_multiple("Luis", "Suarez")
v = operacion(4, 3)
print("El resultado de operacion(4,3) es:", v)
w = operacion()
print("El resultado de operacion() es:", w)
x = op2()
print("El resultado de op2() es:", x)
y = op2(None, 5)
print("El resultado de op2(None, 5) es:", y)
z = op2(5, None)
print("El resultado de op2(5, None) es:", z)
p = op2(a = 5)
print("El resultado de op2(a = 5) es:",p)
q = op2(b = 5)
print("El resultado de op2(b = 5) es:", q)

# Modifica lista1
lista1 = ["Ana", "Maria", "Luis", "Elena"]
fun_lista(lista1, "Andres")
print("lista1:", lista1) 

# Crea otra lista, pero la lista que es argumento 
# de entrada no cambia
lista2 = ["Marte", "Jupiter", "Saturno"]
lista3 = ["Urano", "Tierra"]
lista4 = []
fun_list2(lista3, lista2)
fun_list2(lista4, lista2)
print("lista2:", lista2)
print("lista3:", lista3)
print("lista4:", lista4)