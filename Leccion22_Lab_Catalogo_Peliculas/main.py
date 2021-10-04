# Leccion 22 - Catalogo de peliculas
# ----------------------------------

from catalogoPeliculas import catalogoPeliculas as cp
from pelicula import Pelicula
#import os
# os.remove(filename)

if __name__ == '__main__':
    opcion = None
    while opcion != 4:
        try:
            print('Opciones: ')
            print('1 - Agregar Pelicula')
            print('2 - Listar Peliculas')
            print('3 - Eliminar Archivo')
            print('4 - Salir')
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                nombrePelicula = input("Introduce el nombre de la pelicula: ")
                pelicula = Pelicula(nombrePelicula)
                cp.agregarPelicula(pelicula)
            elif opcion == 2:
                cp.listarPeliculas()
            elif opcion == 3:
            	cp.eliminarPeliculas()
            	
        except Exception as e:
            print(f'Ocurrio un error: {e}')
            opcion = None

    else:
        print("Saliendo del programa...")
