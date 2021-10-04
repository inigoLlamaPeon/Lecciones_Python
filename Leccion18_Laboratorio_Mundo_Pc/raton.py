from dispositivoIO import DispositivoIO


class Raton(DispositivoIO):
    cntRaton = 0

    def __init__(self, tipoEntrada, marca):
        Raton.cntRaton += 1
        self._id_raton = Raton.cntRaton
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo de Entrada: {self._tipoEntrada}'


if __name__ == "__main__":
    R1 = Raton('HP', 'USB')
    print(R1)
    print("Numero de teclados", Raton.cntRaton)
    R2 = Teclado('Logitech', 'Inalambrico')
    print(R2)
    print("Numero de teclados", Raton.cntRaton)
