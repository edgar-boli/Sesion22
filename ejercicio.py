def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0 
    

    suma = 0 
    for numero in (numeros):
        suma = suma + numero
        
    cantidad = len(numeros)
    promedio = suma / cantidad
    return promedio

lista_numeros = [5, 10, 15, 20, 25]
resultado = calcular_promedio(lista_numeros)
print(f"El promedio de la lista {lista_numeros} es {resultado}")