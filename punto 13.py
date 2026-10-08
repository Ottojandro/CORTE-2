def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)
n = int(input("Ingrese un número entero positivo: "))
if n<=0:
    print("El número debe ser mayor a cero")
else:
    resultado = contar_digitos(n)
    
print("cantidad de digitos", resultado)