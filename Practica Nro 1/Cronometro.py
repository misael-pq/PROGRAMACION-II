import time
import random


class Cronometro:

    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = None

    def inicia(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia


def seleccion(lista):
    n = len(lista)

    for i in range(n):
        if i % 10000 == 0:  
            print(f"Calculando... {i} / {n}")

        min_i = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_i]:
                min_i = j

        lista[i], lista[min_i] = lista[min_i], lista[i]

#-Desde aqui ya es como la parte fundamental del programa-#
        
print("generando números...")
numeros = [random.randint(0, 1000000) for _ in range(100000)]

print("iniciando cronómetro...")
c = Cronometro()

c.inicia()

print("ordenando por selección... (esto tardará)")
seleccion(numeros)

c.detener()

print("tiempo transcurrido:", c.lapsoDeTiempo(), "ms")
