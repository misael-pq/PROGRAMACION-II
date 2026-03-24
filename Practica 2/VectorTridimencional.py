import math

class VectorTridimensional:
    def __init__(self, a1=0, a2=0, a3=0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def __add__(self, b):
        return VectorTridimensional(
            self.a1 + b.a1,
            self.a2 + b.a2,
            self.a3 + b.a3
        )
    def __mul__(self, r):
        return VectorTridimensional(
            self.a1 * r,
            self.a2 * r,
            self.a3 * r
        )
    def longitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)
    def normal(self):
        mag = self.longitud()
        return VectorTridimensional(
            self.a1 / mag,
            self.a2 / mag,
            self.a3 / mag
        )
    def productoEscalar(self, b):
        return self.a1*b.a1 + self.a2*b.a2 + self.a3*b.a3
    def productoVectorial(self, b):
        return VectorTridimensional(
            self.a2*b.a3 - self.a3*b.a2,
            self.a3*b.a1 - self.a1*b.a3,
            self.a1*b.a2 - self.a2*b.a1
        )
    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"


# CODGO DE PRUEBA
a = VectorTridimensional(1, 2, 3)
b = VectorTridimensional(4, 5, 6)

print("Suma:", a + b)
print("Escalar:", a * 2)
print("Longitud:", a.longitud())
print("Normal:", a.normal())
print("Producto escalar:", a.productoEscalar(b))
print("Producto vectorial:", a.productoVectorial(b))
