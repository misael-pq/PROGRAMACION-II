import math

class AlgebraVectorial:

    def __init__(self, ax=0, ay=0, bx=0, by=0):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by

    def magnitud(self, x, y):
        return math.sqrt(x**2 + y**2)
    def producto_punto(self):
        return self.ax * self.bx + self.ay * self.by
    def perpendicular1(self):
        return self.magnitud(self.ax + self.bx, self.ay + self.by) == \
               self.magnitud(self.ax - self.bx, self.ay - self.by)
    def perpendicular2(self):
        return self.magnitud(self.ax - self.bx, self.ay - self.by) == \
               self.magnitud(self.bx - self.ax, self.by - self.ay)
    def perpendicular3(self):
        return self.producto_punto() == 0
    def perpendicular4(self):
        suma = self.magnitud(self.ax + self.bx, self.ay + self.by)
        magA = self.magnitud(self.ax, self.ay)
        magB = self.magnitud(self.bx, self.by)
        return suma**2 == magA**2 + magB**2
    def paralela1(self):
        if self.bx != 0 and self.by != 0:
            return (self.ax / self.bx) == (self.ay / self.by)
        return False
    def paralela2(self):
        return (self.ax * self.by - self.ay * self.bx) == 0
    def proyeccion(self):
        punto = self.producto_punto()
        magB2 = self.magnitud(self.bx, self.by)**2
        rx = (punto / magB2) * self.bx
        ry = (punto / magB2) * self.by
        return (rx, ry)
    def componente(self):
        return self.producto_punto() / self.magnitud(self.bx, self.by)


v = AlgebraVectorial(2, 3, 4, 6)

print("Perpendicular1:", v.perpendicular1())
print("Perpendicular2:", v.perpendicular2())
print("Perpendicular3:", v.perpendicular3())
print("Perpendicular4:", v.perpendicular4())

print("Paralela1:", v.paralela1())
print("Paralela2:", v.paralela2())

print("Proyeccion:", v.proyeccion())
print("Componente:", v.componente())
