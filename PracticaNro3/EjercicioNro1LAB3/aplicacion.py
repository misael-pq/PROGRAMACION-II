from juego_adivina_numero import JuegoAdivinaNumero

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()


if __name__ == "__main__":
    Aplicacion.main()