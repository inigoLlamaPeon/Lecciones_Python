from dispositivoIO import DispositivoIO


class Teclado(DispositivoIO):
    cntTeclado = 0

    def __init__(self, marca, tipoEntrada):
        Teclado.cntTeclado += 1
        self._idKey = Teclado.cntTeclado
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Id: {self._idKey}, Marca: {self._marca}, Input: {self._tipoEntrada}'


if __name__ == "__main__":
    T1 = Teclado('HP', 'USB')
    print(T1)
    print("Numero de teclados", Teclado.cntTeclado)
    T2 = Teclado('Logitech', 'Inalambrico')
    print(T2)
    print("Numero de teclados", Teclado.cntTeclado)
