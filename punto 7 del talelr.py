calificaciones = (3.2,3.8,3.5,3.1,4.3,5.0)
nota_buscada= float(input("ingrese la nota a buscar"))
cantidad = calificaciones.count(nota_buscada)
print("La nota aparece:", cantidad, "veces")
print("!Recordar que las posiciones inician desde cero¡")
if cantidad>0:
    posicion=calificaciones.index(nota_buscada)
    print("la posicion en la que se encuentra es:", posicion)
else:
    print("La nota no se encuentra en la tupla")