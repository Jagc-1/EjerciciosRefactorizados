#Algoritmo que muestra el área y perímetro de un trapecio

print("-- Area Trapecio --")
print("Base Mayor: ")
B = float(input(":)"))

print("Base Menor: ")
Bh = float(input(":)"))

print("Altura: ")
H = float(input(":)"))


print("------- Perimetro -------")
print("lado 1: ")
l1 = float(input(":)"))
print("lado 2: ")
l2 = float(input(":)"))
print("lado 3: ")
l3 = float(input(":)"))
print("lado 4: ")
l4 = float(input(":)"))


a = ((B * Bh)* H)/2
pe = l1 + l2 +l3 +l4

print("----------------------")
print("Area: ", a, "cm2")
print("Perimetro: ", pe, "cm")
print("----------------------")
