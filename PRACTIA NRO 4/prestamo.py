class Prestamo:
    def __init__(self, e, l):
        self.estudiante = e
        self.libro = l
        self.fecha_prestamo = "Hoy"
        self.fecha_devolucion = "7 dias"

    def mostrarInfo(self):
        print("Estudiante:", self.estudiante.nombre)
        print("Libro:", self.libro.titulo)
        print("Prestamo:", self.fecha_prestamo)
        print("Devolucion:", self.fecha_devolucion)
