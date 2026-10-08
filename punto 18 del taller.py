def contar_recursivo(tupla, valor, indice=0):

    if indice == len(tupla):
        return 0
    else:
       
        if tupla[indice] == valor:
            coincidencia = 1
        else:
            coincidencia = 0
            
        return coincidencia + contar_recursivo(tupla, valor, indice + 1)

entrada = input("Ingrese los números de la tupla separados por espacio: ")
numeros = tuple(map(int, entrada.split()))

buscado = int(input("Ingrese el número que desea contar: "))

res_recursivo = contar_recursivo(numeros, buscado)
res_count = numeros.count(buscado)

print("--- RESULTADOS ---")
print("Conteo con función recursiva:", res_recursivo)
print("Conteo con el método count():", res_count)