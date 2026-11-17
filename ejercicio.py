class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        if self.disponible:
            self.estado = "Disponible"
        else:
            self.estado = "Prestado"
        return f"{self.codigo}-{self.titulo}-{self.autor}-{self.estado}"


class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []


class Biblioteca:
    def __init__(self):
        self.coleccion_de_libros = []
        self.usuarios = []

    def registrar_libro(self, libro):
        self.coleccion_de_libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def consultar_disponibles(self):
        for libro in self.coleccion_de_libros:
            if libro.disponible:
                print(libro)

    def prestar_libro(self, codigo, identificacion):
        for libro in self.coleccion_de_libros:
            if libro.codigo == codigo and libro.disponible:
                for usuario in self.usuarios:
                    if usuario.identificacion == identificacion:
                        libro.disponible = False
                        usuario.libros_prestados.append(libro)
                        print("Libro prestado")
                        return
        print("No se pudo prestar el libro")

    def devolver_libro(self, codigo, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                for libro in usuario.libros_prestados:
                    if libro.codigo == codigo:
                        libro.disponible = True
                        usuario.libros_prestados.remove(libro)
                        print("Libro devuelto")
                        return
        print("No se pudo devolver el libro")


b = Biblioteca()

l1 = Libro("01", "Cien anos de soledad", "Gabriel Garcia Marquez")
l2 = Libro("02", "El principito", "Antoine de Saint Exupery")
u1 = Usuario("Juan", "123")

b.registrar_libro(l1)
b.registrar_libro(l2)
b.registrar_usuario(u1)

b.consultar_disponibles()
b.prestar_libro("01", "123")
b.prestar_libro("01", "123")
b.consultar_disponibles()
b.devolver_libro("01", "123")
b.consultar_disponibles()