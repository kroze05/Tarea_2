"""3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0."""
def relacion(a,b):
    if a>b:
        print("valor devuelto:",1)
    elif a<b:
        print("valor devuelto:",-1)
    else:
        print("valor devuelto:",0)

a=int(input("introduzca un numero\n"))
b=int(input("introduzca el segundo numero\n"))
relacion(a,b)