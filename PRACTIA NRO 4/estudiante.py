class Estudiante:
    def __init__(self, c, n):
        self.codigo = c
        self.nombre = n

    def mostrarInfo(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
