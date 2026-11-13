
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.producto import Producto


class TestProducto(unittest.TestCase):

    def setUp(self):
        self.producto = Producto("P001", "Teclado", 350, 10)

    # CP01: Crear un producto
    def test_CP01_crear_producto(self):
        self.assertEqual(self.producto.id, "P001")
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertEqual(self.producto.precio, 350)
        self.assertEqual(self.producto.cantidad, 10)

    # CP02: Mostrar codigo
    def test_CP02_mostrar_codigo(self):
        self.assertEqual(self.producto.id, "P001")

    # CP03: Mostrar nombre
    def test_CP03_mostrar_nombre(self):
        self.assertEqual(self.producto.nombre, "Teclado")

    # CP04: Mostrar precio
    def test_CP04_mostrar_precio(self):
        self.assertEqual(self.producto.precio, 350)

    # CP05: Mostrar existencia
    def test_CP05_mostrar_existencia(self):
        self.assertEqual(self.producto.cantidad, 10)

    # CP06: Mostrar informacion completa
    def test_CP06_mostrar_informacion_completa(self):
        salida = StringIO()

        with redirect_stdout(salida):
            self.producto.mostrar_producto()

        resultado = salida.getvalue()

        self.assertIn("P001", resultado)
        self.assertIn("Teclado", resultado)
        self.assertIn("Precio: $ 350\n", resultado)
        self.assertIn("10", resultado)

    # CP07: Crear un segundo producto
    def test_CP07_crear_otro_producto(self):
        producto2 = Producto("P002", "Mouse", 180, 5)

        self.assertEqual(producto2.id, "P002")
        self.assertEqual(producto2.nombre, "Mouse")
        self.assertEqual(producto2.precio, 180)
        self.assertEqual(producto2.cantidad, 5)

        self.assertNotEqual(self.producto.id, producto2.id)


if __name__ == "__main__":
    unittest.main()
