# Leccion 6 - Listas, tuplas y diccionarios
# -----------------------------------------


# Lista
# -----

nombres = ['Juan', 'Maria', 'Ana', 'Luis'] # Entre corchetes
print("Nombres: ", nombres)
# len(...) nos devuelve la longitud de la lista
print("Longitud de la Lista:", len(nombres))

# Ejemplo 1 - Imprimir los elementos de la lista de 1 en 1.
for i in range(len(nombres)):
    print("Nombre", i, ":", nombres[i])
    
# Ejemplo 2 - Recorrer lista en orden inverso.
# nombres [0] = nombres [-4]
# nombres [1] = nombres [-3]
# nombres [2] = nombres [-2]
# nombres [3] = nombres [-1]
for i in range(-len(nombres), 0):
    print("Nombre", i, ":", nombres[i])  
    
# Ejemplo 3 - Imprimir los dos primeros elementos de la lista.
print("Los dos primeros elementos son:", nombres[0 : 2])
print("Los dos primeros elementos son:", nombres[ : 2])

# Ejemplo 4 - Imprimir los elementos en posiciones pares.
print("Elementos en posiciones pares:", nombres[0 : len(nombres) : 2])

#Ejemplo 5 - Imprimir los elementos desde una posicion hasta el final.
print("Elementos de nombres[1] hasta el final:", nombres[1 : ])

# Operaciones sobre listas

# Sustituir elementos.
nombres[3] = "Marcos"
print("Lista actualizada:", nombres)

# Añadir elemento al final.
nombres.append("Elena")
print("Lista con nuevo nombre:", nombres)

# Añadir elemento en posicion especifica.
nombres.insert(2, "Antonio")
print("Lista con nuevo nombre:", nombres)

# Eliminar elemento de la lista.
nombres.remove("Ana")
print("Lista con nombre eliminado:", nombres)

# Eliminar ultimo elemento de la lista.
nombres.pop()
print("Lista con ultimo elemento eliminado", nombres)

# Eliminar segundo elemento de la lista.
del nombres[1]
print("Lista con nombres[1] eliminado", nombres)

# Borrar elementos de la lista
nombres.clear()
print("nombres.clear():", nombres)

# Eliminar la lista
del nombres
# Si se intenta imprimir la lista, salta un error porque no existe.


# Tuplas
# ------

# A diferencia de la lista, la tupla no se puede modificar

frutas = ("Naranja", "Platano", "Manzana", "Melon", "Fresa")
print ("Tupla:", frutas)
print("Longitud de la tupla:", len(frutas))

# Ejemplo 1 - Imprimir elementos de la tupla
for i in range(0, len(frutas)):
    print("Frutas(", i, "):", frutas[i])

# Ejemplo 2 - Imprimir elementos en orden inverso
for i in range(-len(frutas), 0):
    print("Frutas(", i, "):", frutas[i])

# Ejemplo 3 - Imprimir elementos de la tupla en posiciones pares
print("Posiciones pares:", frutas[0 : len(frutas) : 2])

# Ejemplo 4 - Imprimir desde el segundo elemento hasta el final.
print("Desde segundo elemento:", frutas[1 : ])

# Ejemplo 5 - Imprimir hasta una posicion determinada
print("Hasta posicion 3:", frutas[ : 3])

# Ejemplo 6 - Modificar tupla

# No se pueden modificar los elementos de las tuplas, pero si se
# puede crear una lista a partir de la tupla, modificarla y 
# convertirla en una tupla

frutasLista = list(frutas) # Crear lista a partir de tupla
frutasLista.append("Cereza")
frutasLista.insert(1, "Mango")
frutas = tuple(frutasLista)
print("Tupla actualizada:", frutas)

# Borrar tupla
del frutas

# Sets
# ----

# Es una coleccion sin orden no indice.
# No mantienen ningun orden, sus elementos no se repiten, 
# no pueden modificarse una vez creado, 
# pero si se pueden añadir elementos. 

# Al imprimirse pueden aparecer en distinto orden al declarado
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
print("Tipo de dato:", type(planetas))
print("Dimension:", len(planetas))

# Esta Marte en el set?
print("Marte" in planetas)

# Esta saturno en el set?
print("Saturno" in planetas)

# Añadir el planeta Saturno al set
planetas.add("Saturno")
print(planetas)

# Eliminar elemento
planetas.remove("Saturno")
print(planetas)

planetas.discard("Marte")
print(planetas)

# Limpiar el set
planetas.clear()
print(planetas)

# Eliminar set
del planetas


# Diccionarios
# ------------

# Diccionario compuesto por variable y valor (key & value)

diccionario = {
    "IDE" : "Integrated Development Enviroment",
    "OOP" : "Object Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)
print("Dimensiones:", len(diccionario))

# Acceder a elementos del diccionario
print(diccionario["IDE"])
print(diccionario.get("IDE"))

# Modificar variable
diccionario["IDE"] = "integrated development environment"
print(diccionario["IDE"])

# Reccorido de diccionario con bucle for

for termino in diccionario:
    print(termino)              # Llave
    print(diccionario[termino]) # Valor
    
for valor in diccionario.values():
    print(valor)                # Valor
    
# Comprobar existencia en diccionario
print("IDE" in diccionario)
print("IDE" in diccionario.keys()) # Equivalente
print("integrated development environment" in diccionario.values())

# Agregar elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

# Eliminar elementos
diccionario.pop("DBMS")
print(diccionario)

# Limpiar diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
# print(diccionario)