numeros=(24,34,23,18,47,82,14,20)
suma = 0
for nota in numeros:
    suma = suma + nota
promedio = suma/ len(numeros)
maximo=max(numeros)
minimo=min(numeros)

print("promedio:",promedio)
print("suma:",suma)
print("numero mayor", maximo)
print("numero menor", minimo)