#5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
while True:
    lista = [0,1,2,3,4,5,6,7,8,9]
    print(lista)
    val=int(input("ingresa un valor que se encuentre en la lista\n"))
    if val in lista:
        print(f"la variable introducida {val} si se encuentra entre {lista}")
        break
    else:
        print(f"la variable introducida {val} no se encuentra entre {lista}, vuelva a intentarlo")