import math


class Estadistica:

    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        prom = self.promedio()

        suma = 0
        for x in self.datos:
            suma += (x - prom) ** 2

        return math.sqrt(suma / (len(self.datos) - 1))


print("Ingrese 10 números:")
datos = list(map(float, input().split()))

est = Estadistica(datos)

print("El promedio es", round(est.promedio(), 2))
print("La desviación estándar es", round(est.desviacion(), 5))













