#os: para archivos del sistema
import os

# Clase Pelicula
class Pelicula:
    def __init__(self, nombre):
        # Atributo privado
        self.__nombre = nombre

    # Método para obtener el nombre de la película
    def get_nombre(self):
        return self.__nombre


# Clase CatalogoPeliculas
class CatalogoPeliculas:
    def __init__(self, nombre):
        # Guardamos el nombre del catálogo
        self.nombre = nombre
        # Ruta del archivo txt
        self.ruta_archivo = nombre + ".txt"

        # Verificamos si el archivo ya existe
        if not os.path.exists(self.ruta_archivo):
            # Si no existe, lo creamos vacío
            with open(self.ruta_archivo, "w") as archivo:
                pass  # No se hace nada dentro

    # Método para agregar una película al catálogo
    def agregar(self, pelicula):
        # Abrimos el archivo en modo "a" (agregar al final)
        with open(self.ruta_archivo, "a") as archivo:
            # Escribimos el nombre de la película en una nueva línea
            archivo.write(pelicula.get_nombre() + "\n")
        print(f"La película '{pelicula.get_nombre()}' fue agregada al catálogo.")

    # Método para listar todas las películas guardadas
    def listar(self):
        print("\nPelículas en el catálogo:")
        # Verificamos si el archivo existe
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "r") as archivo:
                # Leemos todas las líneas del archivo (cada línea es una película)
                peliculas = archivo.readlines()
                if peliculas:
                    # Recorremos y mostramos cada película
                    for i, peli in enumerate(peliculas, 1):
                        print(f"{i}. {peli.strip()}")  # strip: quita los saltos de línea
                else:
                    print("El catálogo está vacío.")
        else:
            print("El catálogo no existe.")

    # Método para eliminar el archivo del catálogo
    def eliminar(self):
        # verificamos si el archivo existe
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)  # eliminamos el archivo
            print("Catálogo eliminado correctamente.")
        else:
            print("El catálogo no existe para eliminar.")
