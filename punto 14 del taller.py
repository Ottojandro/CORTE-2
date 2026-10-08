def sumar_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sumar_digitos(n // 10)
n = int(input("Ingrese un número entero positivo: "))
if n<=0:
    print("El número debe ser mayor a cero")
else:
    resultado = sumar_digitos(n)
    
print("suma de digitos", resultado)