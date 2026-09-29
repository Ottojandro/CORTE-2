palabra= input("ingrese una palabra:")
tupla_caracteres = tuple(palabra)
print(tupla_caracteres)
contador = 0
for letra in tupla_caracteres:
    if letra.lower() == 'a':
        contador = contador + 1
print("La letra 'a' aparece:", contador, "veces")        
