import json


class Libreria:
    """
    Clase que representa una librería virtual.

    Atributos:
        libros (list): Lista de diccionarios que representan los libros de la
        librería.

    Métodos:
        __init__(self): Constructor de la clase.
        anadir_libro(self, titulo, autor, genero, anio): Añade un libro a la
        librería.
        buscar_libro(self, titulo): Busca un libro por su título.
        buscar_por_autor(self, autor): Busca libros por un autor.
        eliminar_libro(self, titulo): Elimina un libro por su título.
        guardar_libros(self, archivo): Guarda la colección de libros en un
        archivo JSON.
        cargar_libros(self, archivo): Carga la colección de libros desde un
        archivo JSON.
    """

    def __init__(self):
        """Constructor de la clase.

        Inicializa la lista de libros con una lista vacía.
        """
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la librería.

        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            genero (str): Género del libro.
            anio (int): Año de publicación del libro.

        Returns:
            str: Mensaje de confirmación o error.
        """
        try:
            anio = int(anio)  # Asegurarse de que el año sea un entero
        except ValueError:
            return "Año no válido"

        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "anio": anio
        }
        self.libros.append(nuevo_libro)
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Args:
            titulo (str): Título del libro a buscar.

        Returns:
            list: Lista de diccionarios que representan los libros encontrados.
        """
        libros_encontrados = [
            libro for libro in self.libros
            if libro["titulo"].lower() == titulo.lower()
        ]
        return libros_encontrados

    def buscar_por_autor(self, autor):
        """
        Busca libros por un autor.

        Args:
            autor (str): Nombre del autor a buscar.

        Returns:
            list: Lista de diccionarios que representan los libros encontrados.
        """
        libros_encontrados = [
            libro for libro in self.libros
            if autor.lower() in libro["autor"].lower()
        ]
        return libros_encontrados

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por su título.

        Args:
            titulo (str): Título del libro a eliminar.

        Returns:
            str: Mensaje de confirmación o error.
        """
        original_count = len(self.libros)
        self.libros = [
            libro for libro in self.libros
            if libro["titulo"].lower() != titulo.lower()
        ]
        if len(self.libros) < original_count:
            return "Libro eliminado"
        else:
            return "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la colección de libros en un archivo JSON.

        Args:
            archivo (str): Ruta del archivo JSON donde se guardarán los libros.

        Returns:
            str: Mensaje de confirmación.
        """
        try:
            with open(archivo, "w") as f:
                json.dump(self.libros, f, indent=4)
            return "Libros guardados"
        except IOError as e:
            return f"Error al guardar los libros: {e}"

    def cargar_libros(self, archivo):
        """
        Carga la colección de libros desde un archivo JSON.

        Args:
            archivo (str): Ruta del archivo JSON donde se encuentran los libros.

        Returns:
            str: Mensaje de confirmación o error.
        """
        try:
            with open(archivo, "r") as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"
        except json.JSONDecodeError:
            return "Error al leer el archivo JSON"


if __name__ == "__main__":
    mi_libreria = Libreria()
    print(mi_libreria.anadir_libro(
        "Cien años de soledad", "Gabriel García Márquez", "Novela", 1967))
    print(mi_libreria.anadir_libro(
        "El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela",
        1985))

    print("Buscar libro por título:")
    print(mi_libreria.buscar_libro("Cien años de soledad"))

    print("Buscar libros por autor:")
    print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))

    print("Eliminar libro:")
    print(mi_libreria.eliminar_libro("Cien años de soledad"))

    print("Guardar libros:")
    print(mi_libreria.guardar_libros("libros.json"))

    print("Cargar libros:")
    print(mi_libreria.cargar_libros("libros.json"))

    print("Contenido de la librería después de cargar:")
    print(mi_libreria.libros)
