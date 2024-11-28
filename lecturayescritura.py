with open("hola.txt", "r") as archivo:
    contenido = archivo.read()

contenido += "\nedgar"


with open("hola.txt", "w") as archivo:
    archivo.write(contenido)
    