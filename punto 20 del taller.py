ventas = (("Cuaderno", 3, 8500),("Lapiz", 5, 1500),("Regla", 2, 4000))

def calcular_total_recursivo(ventas, indice=0):
    if indice == len(ventas):
        return 0
    else:
        producto = ventas[indice]
        subtotal = producto[1] * producto[2]
        return subtotal + calcular_total_recursivo(ventas, indice + 1)

total_vendido = calcular_total_recursivo(ventas)

unidades_totales = sum(item[1] for item in ventas)

producto_mayor = ventas[0]
max_ingreso = producto_mayor[1] * producto_mayor[2]

for producto in ventas:
    ingreso_actual = producto[1] * producto[2]
    if ingreso_actual > max_ingreso:
        max_ingreso = ingreso_actual
        producto_mayor = producto

promedio_ingreso = total_vendido / len(ventas)

print("1. Valor total vendido: $", total_vendido)
print("2. Cantidad total de unidades vendidas:", unidades_totales)
print("3. Producto con mayor ingreso:", producto_mayor[0], "($", max_ingreso, ")")
print("4. Promedio de ingreso por producto: $", promedio_ingreso)