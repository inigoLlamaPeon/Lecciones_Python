# Leccion 20 - Manejo de Archivos
# -------------------------------

# Si el archivo no existe, se crea
# automaticamente

# 'w' : Crear y escribe en archivo
# 'w+': Escribir y leer
# 'r' : Lee archivo. Da error si no existe
# 'r+': Identico a 'w+'?
# 'a' : Añade texto al archivo
# 'x' : Crea un archivo y da error si ya existe
# 't' : Modo texto. Modo por defecto
# 'b' : Modo binario (imagenes)

try:
    archivo = open('prueba.txt', 'w', encoding='utf-8')
    archivo.write("Hola Mundo\n")
    archivo.write("Adiós Mundo\n")
except Exception as e:
    print(e)
finally:
    archivo.close()
    print(f'Archivo cerrado')

archivo = open('prueba.txt', 'r', encoding='utf-8')
# print(archivo.read()) # Lee todo el archivo
print(archivo.read(7))  # Lee los 7 primeros caracteres
print(archivo.read(3))  # Lee los siguientes caracteres
archivo.close()
print("------------------------")

archivo = open('prueba.txt', 'r', encoding='utf-8')
for linea in archivo:
    print(linea)
archivo.close()
print("------------------------")

archivo = open('prueba.txt', 'r', encoding='utf-8')
# archivo.readlines() # Crea una lista
print('archivo.readlines()[1]: ', archivo.readlines()[1])
archivo.close()
print("------------------------")

archivo = open('prueba.txt', 'r', encoding='utf-8')
archivo2 = open('copia.txt', 'a', encoding='utf-8')
archivo2.write("Linea 1 de la copia\n")
archivo2.write(archivo.read())
# Cambiar modo para leer el nuevo archivo
archivo2 = open('copia.txt', 'r', encoding='utf-8')
print(archivo2.readlines())
archivo2.close()