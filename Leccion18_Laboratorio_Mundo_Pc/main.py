from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado
from orden import Orden

if __name__ == "__main__":
    t1 = Teclado('HP', 'USB')
    t2 = Teclado('Logitech', 'Inalambrico')
    m1 = Monitor("LG", 27)
    m2 = Monitor("MSI", 24)
    r1 = Raton('HP', 'USB')
    r2 = Teclado('Logitech', 'Inalambrico')
    c1 = Computadora("HP", m1, t1, r1)
    c2 = Computadora("Toshiba", m2, t2, r2)
    compus = [c1, c2]
    orden1 = Orden(compus)
    print(orden1)

    t3 = Teclado("Gaming", "Cable")
    m3 = Monitor("Samsung", 21)
    r3 = Raton("Razor", "Bluetooth")
    c3 = Computadora("Asus", m3, t3, r3)

    orden1.addPc(c3)
    print(orden1)