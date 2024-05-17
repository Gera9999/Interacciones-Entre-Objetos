from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod == producto:
                prod.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        return "\n".join([str(producto) for producto in self.__productos])

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                else:
                    cantidad_vendida = producto.stock
                    producto.stock = 0
                return cantidad_vendida
        return 0

    def __str__(self):
        return f"Tienda: {self.__nombre}, Costo Delivery: {self.__costo_delivery}"

class Restaurante(Tienda):
    def ingresar_producto(self, producto):
        producto.stock = 0
        super().ingresar_producto(producto)

    def listar_productos(self):
        return "\n".join([f"{producto.nombre} - ${producto.precio}" for producto in self._Tienda__productos])

    def realizar_venta(self, nombre_producto, cantidad):
        pass  # No stock management for Restaurante

class Supermercado(Tienda):
    def listar_productos(self):
        productos = []
        for producto in self._Tienda__productos:
            stock_msg = f"Pocos productos disponibles ({producto.stock})" if producto.stock < 10 else f"Stock: {producto.stock}"
            productos.append(f"{producto.nombre} - ${producto.precio} - {stock_msg}")
        return "\n".join(productos)

class Farmacia(Tienda):
    def listar_productos(self):
        productos = []
        for producto in self._Tienda__productos:
            precio_msg = "Envío gratis al solicitar este producto" if producto.precio > 15000 else ""
            productos.append(f"{producto.nombre} - ${producto.precio} - {precio_msg}")
        return "\n".join(productos)

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            return 0
        return super().realizar_venta(nombre_producto, cantidad)
