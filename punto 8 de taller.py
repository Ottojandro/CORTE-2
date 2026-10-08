productos=(("cuaderno", 8500,5),("audifonos", 20000,2), ("lapiz",3000,5))

total_inventario=0

for producto in productos:
    nombre,precio,cantidad = producto
    subtotal= precio * cantidad
    total_inventario= total_inventario + subtotal
    print("Producto:", nombre, "|cantidad|",cantidad,"|precio normal|", precio,"|precio final|", subtotal)
   
print("Valor total del inventario:", total_inventario)