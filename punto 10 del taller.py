def suma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)

n = int(input("Ingrese un número natural (n): "))

if n > 0:
    resultado = suma_recursiva(n)
    print("La suma de los números desde 1 hasta", n, "es:", resultado)
else:
    print("Por favor, ingrese un número mayor a 0.")