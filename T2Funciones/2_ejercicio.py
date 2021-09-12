#2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:
import math
def area_circulo(radio):
    res= math.pi*(radio**2)
    print(f"el area del circulo con radio de {radio} es {res}")
area_circulo(5)