# Muestra el producto de varios números ingresados

pro = 1

print("valor de N:")
n = int(input(":)"))

for f in range(1, n + 1):
    print(f, end=" ")
    pro = pro * f
print(f"\nEl producto de los {n} números es: {pro}")
