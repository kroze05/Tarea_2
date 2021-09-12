#6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:
def separar(*args):
    lista_pares = []
    lista_inpares = []
    for i in args:
        pi=i%2
        if pi == 1:
            lista_pares.append(i)
        else:
            lista_inpares.append(i)
    print("lista pares ordenados: ",lista_pares)
    print("lista inpares ordenados: ",lista_inpares)
args = input("introduzca los valores que desea separar separados por una coma\n").split(",")
lista=[]
for val in args:
    val=int(val)
    lista.append(val)
lista.sort()
print("lista ordenada: ",lista)
separar(*lista)