#6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
#Todos los números del 0 al 10 [0, 1, 2, ..., 10]
val = []
for i in range(0,11):
    val.append(i)
print("los numeros del 1 al 10 son: ",val)
#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
val = []
for i in range(-10,1):
    val.append(i)
print("los numeros del -10 al 0 son: ",val)
#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
val = []
for i in range(0,21,2):
    val.append(i)
print("los numeros del 0 al 20 pares son: ",val)
#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
val = []
for i in range(-21,1,2):
    val.append(i)
print("los numeros del -20 al 0 impares son: ",val)
#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
val = []
for i in range(0,51,5):
    val.append(i)
print("los numeros multiplos del 5 del 0 al 50 son: ",val)