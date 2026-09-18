nombres=("Alejandro","Omar","Juan","Julian","niñas")

print(nombres[0])
print(nombres[-1])



numeros = (7,2,5,8,9,10,2026)

suma = 0
for nota in numeros:
    suma = suma + nota
print("suma:",suma)



notas = (3.8,4.5,1.1,3.0,3.2)

suma = 0
for nota in notas:
    suma = suma + nota
    
promedio = suma/ len(notas)
print("promedio:",promedio)




edades = (18,16,15,20,21)
resul = 0
for edad in edades:
    if edad >= 18:
        resul = resul +1
        
print("mayor:",resul)