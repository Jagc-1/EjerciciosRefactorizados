#Algoritmo que muestre la tabla de multiplicar de cualquier número.


print("------------------------------------")
print("ingrese un número:")
num =  int(input(":)"))
print(f"---- Aqui esta la tabla del {num} ------")

for cont in range(12):
    cont +=1
    print(num, " x ", cont, " = ", (num*cont))
print("------------------------------------")
