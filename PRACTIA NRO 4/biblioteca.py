class Biblioteca:
    def __init__(self, n):
        self.nombre = n
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = Horario("Lunes a Viernes", "08:00", "18:00")

    def agregarLibro(self, l):
        self.libros.append(l)

    def agregarAutor(self, a):
        self.autores.append(a)

    def prestarLibro(self, e, l):
        p = Prestamo(e, l)
        self.prestamos.append(p)

    def mostrarEstado(self):
        print("Biblioteca:", self.nombre)
        self.horario.mostrarHorario()

        print("Libros:")
        for x in self.libros:
            print("-", x.titulo)

        print("Autores:")
        for x in self.autores:
            print("-", x.nombre)

        print("Prestamos:")
        for x in self.prestamos:
            x.mostrarInfo()

    def cerrarBiblioteca(self):
        print("La biblioteca esta cerrada")
        self.prestamos = []
