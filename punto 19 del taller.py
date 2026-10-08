def buscar_estudiante(tupla, nombre, indice=0):
    if indice == len(tupla):
        return -1
    elif tupla[indice] == nombre:
        return indice
    else:
        return buscar_estudiante(tupla, nombre, indice + 1)
    
estudiantes = ("Ana", "Carlos", "María", "Juan", "Sofía")
buscado = input("Ingrese el nombre del estudiante a buscar: ")
posicion = buscar_estudiante(estudiantes, buscado)
if posicion != -1:
    print("El estudiante se encuentra en la posición:", posicion)
else:
    print("El estudiante no existe en la lista")