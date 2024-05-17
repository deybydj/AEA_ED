import unittest
import os

from libreria import Libreria

class TestLibreria(unittest.TestCase):
    def setUp(self):
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.anadir_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", 1985)

    def tearDown(self):
        if os.path.exists("libros.json"):
            os.remove("libros.json")

    def test_anadir_libro(self):
        self.assertEqual(self.libreria.anadir_libro("El perfume", "Patrick Süskind", "Novela", 1985), "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 3)  # Se agregó un libro, así que la longitud debe ser 3

    def test_buscar_libro(self):
        self.assertEqual(len(self.libreria.buscar_libro("Cien años de soledad")), 1)
        self.assertEqual(len(self.libreria.buscar_libro("El perfume")), 0)

    def test_buscar_por_autor(self):
        self.assertEqual(len(self.libreria.buscar_por_autor("Gabriel García Márquez")), 2)
        self.assertEqual(len(self.libreria.buscar_por_autor("Patrick Süskind")), 0)

    def test_eliminar_libro(self):
        self.assertEqual(self.libreria.eliminar_libro("Cien años de soledad"), "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 1)  # Se eliminó un libro, así que la longitud debe ser 1

    def test_guardar_cargar_libros(self):
        self.assertEqual(self.libreria.guardar_libros("libros.json"), "Libros guardados")
        self.assertTrue(os.path.exists("libros.json"))  # Verificar si el archivo se ha creado

        # Crear una nueva instancia de la librería
        nueva_libreria = Libreria()
        self.assertEqual(self.libreria.cargar_libros("libros.json"), "Libros cargados")
        self.assertEqual(len(nueva_libreria.libros), 2)  # Verificar si se cargaron los libros correctamente

if __name__ == "__main__":
    unittest.main()
