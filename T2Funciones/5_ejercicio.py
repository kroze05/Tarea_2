#5) Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
def recortar(numero_recortar, limite_inferior, limite_superior):
    if  numero_recortar < limite_inferior:
        return limite_inferior
    elif  numero_recortar > limite_superior:
        return limite_superior
    return numero_recortar

numero_recortar = int(input("Ingrese el numero:\n"))
limite_inferior = int(input("Ingrese el limite inferior:\n"))
limite_superior = int(input("Ingrese el limite superior:\n"))
print(f"El resultado es = {recortar(numero_recortar, limite_inferior, limite_superior)}")