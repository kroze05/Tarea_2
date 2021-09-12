#7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:
val_1 = list(map(str,input("ingrese una lista de elementos separados por coma\n").split(",")))
val_2 = list(map(str,input("ingrese otra lista de elementos separados por comas\n").split(",")))
print(val_1)
print(val_2)
val_to=[]
for i in val_1 and val_2:
    val_to += i
print(f"los elementos repetidos de la lista son:{val_to}")