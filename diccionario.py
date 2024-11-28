lista = []
nombre = ["jose", "pedro", "andres", "carlos", "ana", "juana", "carmen", "camila", "juan", "ledys"]
dic = {}
n = 10
def unnombre (d,c,v):
    d[c] = v



for i in range(n):
    lista.append (i+1)
    unnombre(dic,nombre[i],lista[i])

print(nombre)
print(lista)
print(dic)

