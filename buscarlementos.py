# Crear un diccionario para el almacenar estudiantes y sus notas 

diccionario_estudiantes = {}


def agregar_estudiante(diccionario, nombre, nota):
    diccionario[nombre] = nota



def calcular_promedio_nota(diccionario):
    if len(diccionario) == 0:
        return 0
    suma_nota = 0 
    for nota in diccionario.valores():
        suma_nota += nota
    return suma_nota / len(diccionario)


promedio = calcular_promedio_nota(diccionario_estudiantes)
print(f"El promedio de las notas es", promedio)
