def invertir_cadena(cadena):
# Caso base: si la cadena tiene 0 o 1 carácter, ya está invertida.
    if len(cadena) <= 1:
        return cadena
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]
    
cadena = input("Ingrese una palabra o frase: ")
resultado = invertir_cadena(cadena)
print("La cadena invertida es:", resultado)
        