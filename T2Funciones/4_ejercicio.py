#4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
def intermedio(a,b):
    suma=a+b
    suma/=2
    print(f"el numero intermedio entre {a} y {b} es",suma)

val_1=int(input("coloca un numero\n"))
val_2=int(input("coloca otro numero\n"))
intermedio(val_1,val_2)