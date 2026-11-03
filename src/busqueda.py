# Sistema de Inventario
# Funcionalidad: Busqueda de productos

def buscar_productos(productos, nombre):
    resultados = []

    for producto in productos:
        if nombre.lower() in producto["nombre"].lower():
            resultados.append(producto)

    return resultados


# Lista de productos del inventario
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 15000},
    {"id": 2, "nombre": "Mouse", "precio": 250},
    {"id": 3, "nombre": "Teclado", "precio": 500},
    {"id": 4, "nombre": "Laptop Gamer", "precio": 25000}
]

# Buscar productos
nombre_buscar = input("Ingrese el producto a buscar: ")

resultados = buscar_productos(productos, nombre_buscar.strip())

if resultados:
    print("\nProductos encontrados:")

    for producto in resultados:
        print("ID:", producto["id"])
        print("Nombre:", producto["nombre"])
        print("Precio: $", producto["precio"])
        print("-----------------------")
else:
    print("No se encontraron productos.")