class Monitor:
    cntMonitor = 0

    def __init__(self, marca, tamano):
        Monitor.cntMonitor += 1
        self._idMon = Monitor.cntMonitor
        self._marca = marca
        self._tamano = tamano

    def __str__(self):
        return f'Id: {self._idMon}, Marca: {self._marca}, Tamaño: {self._tamano}'


if __name__ == "__main__":
    M1 = Monitor("LG", 27)
    print("Numero de monitores", Monitor.cntMonitor)
    print(M1)
    M2 = Monitor("MSI", 24)
    print("Numero de monitores", Monitor.cntMonitor)
    print(M2)
