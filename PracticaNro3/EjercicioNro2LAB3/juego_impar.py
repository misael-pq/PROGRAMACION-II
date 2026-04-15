from juego_adivina_numero import JuegoAdivinaNumero

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            if numero % 2 != 0:
                return True
            else:
                print("Error: el numero debe ser IMPAR")
                return False
        else:
            print("Numero fuera de rango")
            return False