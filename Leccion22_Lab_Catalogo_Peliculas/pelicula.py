# Clase Pelicula

class Pelicula:
    cntPeli = 0
    def __init__(self, nombre):
        Pelicula.cntPeli += 1
        self._nombre = nombre
        self._cntPeli = Pelicula.cntPeli
    def __str__(self):
        return f'Nombre de la pelicula {self._cntPeli}:  {self._nombre}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre



if __name__ == '__main__':
    pelicula = Pelicula("Batman")
    print(pelicula)
    pelicula2 = Pelicula("Superman")
    print(pelicula2)
    print(pelicula2._nombre)