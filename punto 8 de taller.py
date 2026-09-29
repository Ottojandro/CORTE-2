productos = (
    ("Cuaderno", 8500, 10),
    ("Lápiz", 1500, 25),
    ("Regla", 4000, 8),
    ("Borrador", 1000, 15)
)

total_inventario = 0

print("=== INVENTARIO DE PRODUCTOS ===")

for producto in productos:
    nombre, precio, cantidad = producto
    valor_subtotal = precio * cantidad
    total_inventario = total_inventario + valor_subtotal
    print("Producto:", nombre, "| Valor inventario:", valor_subtotal)

print("---------------------------------")
print("Valor total del inventario:", total_inventario)