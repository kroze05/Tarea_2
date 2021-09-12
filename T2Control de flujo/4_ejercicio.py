#4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
val = (input("coloque los valores deseados separados por una coma\n"))
val_2=tuple(map(int,val.split(",")))
num = 0
den=len(val_2)
for i in val_2:
    num+=i
print(f"el resultado de sumar todos es: {num} y la media es: {num/den}")