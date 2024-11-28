
lineas = ["linea uno", "linea dos", "linea tres"]


with open("hola.txt", "w") as archivo:
    for linea in lineas:
        archivo.write(linea + '\n') 
