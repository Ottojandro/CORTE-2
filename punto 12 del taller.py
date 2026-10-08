def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente -1)
    
base= int(input("ingrese la el numero por el cual va a hacer la potencia"))
exponente= int(input("ingrese el exponente"))

if exponente < 0:
    print("el exponente debe ser mayo a cero")
else:
    resultado = potencia(base, exponente)

print("la potencia de ",base,"es ",resultado ) 