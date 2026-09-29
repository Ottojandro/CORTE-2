calificaciones = (4.0, 3.5, 5.0, 4.0, 2.5, 4.0, 3.0)
nota_buscada = float(input("Ingrese la nota a buscar: "))
cantidad = calificaciones.count(nota_buscada)
print("La nota aparece:", cantidad, "veces")
if cantidad > 0:
    posicion = calificaciones.index(nota_buscada)
    print("La primera posición en la que se encuentra es:", posicion)
else:
    print("La nota no se encuentra en la tupla.")