#Mostrar los números pares e impares...
par = 0
impar = 0

for cont in range(10):
    print("-------------------")
    print("Número",cont,":",  )
    num =  int(input(":)"))
    if num % 2 == 0:
        par +=1
    else:
        impar +=1
print("-------------------")
print(f"cantidad de Pares: {par} ")
print(f"cantidad de Impares: {impar} ")
