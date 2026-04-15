from juego import Juego
import random

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            return True
        else:
            print("Numero fuera de rango")
            return False

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un numero entre 0 y 10")

        while True:
            intento = int(input("Numero: "))

            if not self.validaNumero(intento):
                continue

            if intento == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                sigue = self.quitaVida()

                if not sigue:
                    break

                if intento < self.numeroAAdivinar:
                    print("Es MAYOR")
                else:
                    print("Es MENOR")