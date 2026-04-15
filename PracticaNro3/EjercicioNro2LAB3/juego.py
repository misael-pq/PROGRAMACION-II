class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        print("\nNueva partida iniciada")

    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")

        if self.numeroDeVidas > 0:
            return True
        else:
            print("Sin vidas")
            return False