from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def crear_tienda():
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ").strip().lower()
    
    if tipo == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo == "farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda inválido.")
        return None

def ingresar_producto(tienda):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto (opcional, por defecto 0): ") or 0)
    producto = Producto(nombre, precio, stock)
    tienda.ingresar_producto(producto)

def listar_productos(tienda):
    print(tienda.listar_productos())

def realizar_venta(tienda):
    nombre_producto = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    tienda.realizar_venta(nombre_producto, cantidad)

def main():
    tienda = crear_tienda()
    if not tienda:
        return

    while True:
        print("\nOpciones:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_producto(tienda)
        elif opcion == "2":
            listar_productos(tienda)
        elif opcion == "3":
            realizar_venta(tienda)
        elif opcion == "4":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
