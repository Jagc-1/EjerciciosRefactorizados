#Calcula la tabla dependiendo del numero que la persona ingrese

print("ingrese un número: ")
num =  int(input(":)"))
print(f"---- Aqui esta la tabla del {num} ------")

for cont in range(10):
    print(num, " x ", cont, " = ", (num*cont))
