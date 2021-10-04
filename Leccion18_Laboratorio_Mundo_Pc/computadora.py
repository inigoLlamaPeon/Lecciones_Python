from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
    cntComputador = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.cntComputador += 1
        self._idComputadora = Computadora.cntComputador
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._idComputadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
        '''


if __name__ == "__main__":
    t1 = Teclado("HP", "Usb")
    r1 = Raton("Logitech", "Bluetooth")
    m1 = Monitor("MSI", 27)
    c1 = Computadora("Asus", m1, t1, r1)
    print(c1)
    print(Computadora.cntComputador)

    t2 = Teclado("Razor", "Usb")
    r2 = Raton("Microsoft", "Cable")
    m2 = Monitor("LG", 19)
    c2 = Computadora("Asus", m2, t2, r2)
    print(c2)
    print(Computadora.cntComputador)
