class Horario:
    def __init__(self, d, ha, hc):
        self.dias = d
        self.hora_apertura = ha
        self.hora_cierre = hc

    def mostrarHorario(self):
        print("Dias:", self.dias)
        print("Apertura:", self.hora_apertura)
        print("Cierre:", self.hora_cierre)
