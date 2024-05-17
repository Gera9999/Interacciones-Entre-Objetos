class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)  # Ensure stock is non-negative

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        self.__stock = max(0, valor)  # Ensure stock is non-negative

    def __add__(self, otro):
        if self == otro:
            return Producto(self.__nombre, self.__precio, self.__stock + otro.__stock)
        return self

    def __sub__(self, cantidad):
        return Producto(self.__nombre, self.__precio, self.__stock - cantidad)

    def __eq__(self, otro):
        return self.__nombre == otro.__nombre

    def __str__(self):
        return f"{self.__nombre} - ${self.__precio}"

    def detalles(self):
        return f"{self.__nombre} - ${self.__precio} - Stock: {self.__stock}"
