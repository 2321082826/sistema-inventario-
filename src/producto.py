
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self):
        print("ID:", self.id)
        print("Nombre:", self.nombre)
        print("Precio: $", self.precio)
        print("Cantidad:", self.cantidad)


# Crear un producto de ejemplo
producto1 = Producto(1, "Laptop", 15000, 5)

# Mostrar información
producto1.mostrar_producto()
