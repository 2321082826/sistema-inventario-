
import unittest
from src.producto import Producto


class TestProducto(unittest.TestCase):

    def test_crear_producto(self):
        producto = Producto(1, "Laptop", 15000, 5)

        self.assertEqual(producto.id, 1)
        self.assertEqual(producto.nombre, "Laptop")
        self.assertEqual(producto.precio, 15000)
        self.assertEqual(producto.cantidad, 5)

    def test_precio_producto(self):
        producto = Producto(2, "Mouse", 250, 10)

        self.assertEqual(producto.precio, 250)

    def test_cantidad_producto(self):
        producto = Producto(3, "Teclado", 500, 8)

        self.assertEqual(producto.cantidad, 8)


if __name__ == "__main__":
    unittest.main()

