from juego import Juego
import random

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAdivinar = random.randint(0, 10)

        print("Adivina un numero entre 0 y 10")

        while True:
            intento = int(input("Numero: "))

            if intento == self.numeroAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                sigue = self.quitaVida()

                if not sigue:
                    break

                if intento < self.numeroAdivinar:
                    print("Es MAYOR")
                else:
                    print("Es MENOR")