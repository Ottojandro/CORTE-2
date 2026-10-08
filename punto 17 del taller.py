def sumar_tupla(tupla, indice):
    if indice == len(tupla):
        return 0
    else:
        return tupla[indice] + sumar_tupla(tupla, indice + 1)
    
entrada = input("Ingrese números enteros separados por espacios: ")
numeros = tuple(map(int, entrada.split()))

resultado = sumar_tupla(numeros, 0)
print("La suma de la tupla es:", resultado)