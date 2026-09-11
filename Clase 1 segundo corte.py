def suma(a,b):
    return a+b
num_1= int(input("Leer num"))
num_2= int(input("Leer num"))
print("resultado suma",suma(num_1,num_2))
     
def resta(a,b):
    return a-b
num_1= int(input("Leer num"))
num_2= int(input("Leer num"))
print("resultado resta",resta(num_1,num_2))

def multiplicacion(a,b):
    return a*b
num_1= int(input("Leer num"))
num_2= int(input("Leer num"))
print("resultado multiplicacion",multiplicacion(num_1,num_2))

def division(a,b):
    return a/b
num_1= int(input("Leer num"))
num_2= int(input("Leer num"))
print("resultado division",division(num_1,num_2))


numeros=[1,7,8,9,3]
for i in range(len(numeros)):
    for j in range(len(numeros)-1):
       if numeros[j]> numeros[j+1]:
           aux=numeros[j]
           numeros[j]= numeros[j+1]
           numeros[j+1]=aux
           print(numeros [j], numeros [j+1], aux)
print(numeros)