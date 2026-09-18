colores=("rojo","azul","verde")
notas = (4.2, 3.8, 5.0)
edades = (18, 20, 22, 19)

print(colores)
print(notas)
print(edades)


numero = (5)
numero2=(5,)

print(type(numero))
print(type(numero2))



frutas=("manzana","pera","mango","uva")

print(frutas[0])
print(frutas[-2])
print(frutas[-1])


dias = ("lunes","martes","miercoles","jueves","vierenes")

for dia in dias:
    print("dia:",dia)
    
    
    
   numeros = (2,4,6,4,8,4)

print(len(numeros))
print(numeros.count(4))
print(numeros.index(8))



estudiante = ("Ana", 18, 4.5)

nombre, edad, promedio = estudiante

print("nombre:", nombre)
print("edad:", edad)
print("promedio:", promedio)



estudiantes = (("Ana", 4.5),("luis",3.8),("maria",4.9))
for nombre, nota in estudiantes:
    print(nombre, "tiene nota", nota)
    
    
    
colores=("roja","azul","verde")

colores[0] = "amarillo"




colores=("rojo","azul","verde")

lista_colores=list(colores)
lista_colores[0]="amarillo"
colores = tuple(lista_colores)

print(colores)






notas = (4.0, 3.5, 5.0, 4.2)

suma = 0
for nota in notas:
    suma = suma + nota
    
promedio = suma/ len(notas)
print("promedio:",promedio)




temperaturas = (18,22,19,25,21)

mayor = temperaturas[0]
menor = temperaturas[0]

for temp in temperaturas:
    if temp > mayor:
        mayor = temp
    if temp < menor:
        menor=temp
        
print("mayor:",mayor)
print("mayor:", menor)
