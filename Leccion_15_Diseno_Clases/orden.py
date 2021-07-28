class Orden:
    contador_ordenes = 0
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)
        
    def agregar(self, producto):
        self._productos.append(producto)
        
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto._precio
        return total
    
    def __str__(self):
        producto_str = ''
        for producto in self._productos:
            producto_str += producto.__str__() + '|'
        return f'Orden: {self._id_orden}, Productos: {producto_str}'
        