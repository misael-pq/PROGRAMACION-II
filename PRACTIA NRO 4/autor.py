class Autor:
    def __init__(self, n, na):
        self.nombre = n
        self.nacionalidad = na

    def mostrarInfo(self):
        print("Autor:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
