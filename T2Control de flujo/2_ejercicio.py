#2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
while True:
    val = int(input("introduce un numero impar para completar la función\n"))
    val %= 2
    if val == 1:
        print("el programa se ha ejecutado correctamente\n")
        break
    else:
        print("numero incorrecto, vuelva a intentar")