import os
from pelicula import Pelicula

class catalogoPeliculas:
	ruta_archivo = 'peliculas.txt'

	@classmethod
	def agregarPelicula(cls, pelicula):
		with open(cls.ruta_archivo, 'a', encoding='utf-8') as archivo:
			archivo.write(f'{pelicula.nombre}\n')

	@classmethod
	def listarPeliculas(cls):
		with open(cls.ruta_archivo, 'r', encoding='utf-8') as archivo:
			print("Catalogo de peliculas".center(50, '-'))
			print(archivo.read())

	@classmethod
	def eliminarPeliculas(cls):
		os.remove(cls.ruta_archivo)
		print("Archivo eliminado")


if __name__ == '__main__':
    pelicula = Pelicula("Batman")
    print(pelicula)
    pelicula2 = Pelicula("Superman")
    print(pelicula2)
    print(pelicula2._nombre)