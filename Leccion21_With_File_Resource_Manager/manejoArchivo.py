class manejoArchivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print("Obtenemos el archivo".center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf-8')
        return self.nombre

    def __exit__(self, tipoException, valorException, trazaError):
    	print("Cerramos el archivo".center(50, '-'))
    	if self.nombre:
    		self.nombre.close()