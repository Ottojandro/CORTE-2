def suma_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n - 1)  

n = int(input("Ingrese un número natural (n): "))

resultado = suma_naturales(n)
print("La suma de los números naturales es:", resultado)