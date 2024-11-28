
try:
    with open("archivo_prueba.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileExistsError:
    print("El archivo no existe. . .")
except IOError:
    print("Ocurrió un error al leer el archivo. . .")
