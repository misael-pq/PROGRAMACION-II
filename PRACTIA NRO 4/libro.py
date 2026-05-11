class Libro:
    def __init__(self, t, i, p):
        self.titulo = t
        self.isbn = i
        self.paginas = []

        num = 1
        for x in p:
            self.paginas.append(Pagina(num, x))
            num += 1

    def leer(self):
        print("Titulo:", self.titulo)
        print("ISBN:", self.isbn)
        for x in self.paginas:
            x.mostrarPagina()
