from juego_adivina_numero import JuegoAdivinaNumero
from juego_par import JuegoAdivinaPar
from juego_impar import JuegoAdivinaImpar

class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)

        juego1.juega()
        juego2.juega()
        juego3.juega()


if __name__ == "__main__":
    Aplicacion.main()