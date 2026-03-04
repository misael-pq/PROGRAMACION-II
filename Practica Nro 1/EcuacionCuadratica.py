import math

class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c

    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.b + math.sqrt(disc)) / (2*self.a)

    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.b - math.sqrt(disc)) / (2*self.a)


#aqui va la parte de prueba#
print("ingrese a, b, c:")
a, b, c = map(float, input().split())
ecu = EcuacionCuadratica(a, b, c)
disc = ecu.getDiscriminante()

if disc > 0:
    print("La ecuación tiene dos raíces",
          ecu.getRaiz1(), "y", ecu.getRaiz2())

elif disc == 0:
    print("La ecuación tiene una raíz",
          ecu.getRaiz1())

else:
    print("La ecuación no tiene raíces reales")
