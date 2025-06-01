from Ugarte_Dario_Ismael import Pelicula, CatalogoPeliculas

def menu():
    print("\nMenu de opciones:")
    print("1. Agregar pelicula")
    print("2. Listar pelicula")
    print("3. Eliminar catalogo de peliculas")
    print("4. Salir")

# Inicio del programa
nombre_catalogo = input("Ingrese el nombre del catalogo: ")
catalogo = CatalogoPeliculas(nombre_catalogo)

while True:
    menu()
    opcion = input("Seleccione una opcion (1-4): ")

    if opcion == "1":
        nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
        peli = Pelicula(nombre_pelicula)
        catalogo.agregar(peli)
    elif opcion == "2":
        catalogo.listar()
    elif opcion == "3":
        catalogo.eliminar()
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida, elija una opcion del 1 al 4.")