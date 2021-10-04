# Leccion 21 - With, Arhivos y Resource Manager
# ---------------------------------------------

from manejoArchivo import manejoArchivo
# Usar solo si existe el archivo. El archivo
# se cierra automaticamente al finalizar

#with open('prueba.txt', 'r', encoding='utf-8') as archivo:
with manejoArchivo('prueba.txt') as archivo:
	print(archivo.read())

