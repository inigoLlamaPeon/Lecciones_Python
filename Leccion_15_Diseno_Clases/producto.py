class Producto:
    # Variable Pública
    contador_productos = 0
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        # Variable Encapsuladas -> Agregar guión bajo al principio
        self.id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    @property
    def precio(self):
        return self._precio
    
    def __str__(self):
        return f'Id Producto: {self.id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'