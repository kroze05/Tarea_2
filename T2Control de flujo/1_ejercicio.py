#1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
num_1=int(input("introduzca un numero\n"))
num_2=int(input("introduzca otro numero\n"))
print("""
1. Suma de los numeros
2. Resta de los numeros (el primero menos el segundo)
3. Multiplicacion de los numeros
""")
men=int(input("seleccione que desea hacer con los numeros introducidos\n"))
if men ==1:
    total= num_1+ num_2
    print(f"el resutado de {num_1}+{num_2} es {total}")
elif men==2:
    total=num_1-num_2
    print(f"el resultado de la resta entre el primero {num_1} con el segundo {num_2} es{total}")
elif men==3:
    total= num_1* num_2
    print(f"el resutado de {num_1}*{num_2} es {total}")
else:
    print("los caracteres introducidos no son validos,intente de nuevo")