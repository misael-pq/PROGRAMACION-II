from pagina import Pagina
from horario import Horario
from autor import Autor
from estudiante import Estudiante
from libro import Libro
from prestamo import Prestamo
from biblioteca import Biblioteca

p1 = ["Inicio del libro", "Capitulo 1", "Capitulo 2"]
l1 = Libro("Python Basico", "12345", p1)
a1 = Autor("Juan Perez", "Bolivia")
e1 = Estudiante("2024001", "Misael")
b1 = Biblioteca("Biblioteca UMSA")
b1.agregarLibro(l1)
b1.agregarAutor(a1)
b1.prestarLibro(e1, l1)

print("\nESTADO DE LA BIBLIOTECA\n")
b1.mostrarEstado()
print("\nLEYENDO LIBRO\n")
l1.leer()
print("\nDATOS DEL AUTOR\n")
a1.mostrarInfo()
print("\nDATOS DEL ESTUDIANTE\n")
e1.mostrarInfo()

b1.cerrarBiblioteca()

print("\nESTADO FINAL\n")
b1.mostrarEstado()
