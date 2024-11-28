# Lectura de un Archivo

# Abrir el Archivo en Modo Lectura 
with open("hola.txt", "r") as archivo:
    # Leer cada linea del archivo
    for linea in archivo:
        print(linea.strip())  # Imprimir la linea sin caracteres de salto de linea 

