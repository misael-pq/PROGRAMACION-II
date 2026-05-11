class Pagina:
    def __init__(self, n, c):
        self.numero = n
        self.contenido = c

    def mostrarPagina(self):
        print("Pagina:", self.numero)
        print("Contenido:", self.contenido)
