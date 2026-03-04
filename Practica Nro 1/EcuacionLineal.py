class EcuacionLineal:

    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def tieneSolucion(self):
        return (self.a * self.d - self.b * self.c) != 0

    def getX(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)

    def getY(self):
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)



print("ingrese a, b, c, d, e, f:")
a, b, c, d, e, f = map(float, input().split())

ecu = EcuacionLineal(a, b, c, d, e, f)

if ecu.tieneSolucion():
    print("x =", ecu.getX(), ", y =", ecu.getY())
else:
    print("La ecuación no tiene solución")
