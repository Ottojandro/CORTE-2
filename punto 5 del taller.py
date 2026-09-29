dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
numero = int(input("Ingrese un número entre 1 y 7: "))

if 1 <= numero <= 7:
    print("El dia correspondiente es", dias[numero - 1])
else:
    print("El número debe estar entre 1 y 7")