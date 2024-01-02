#Algoritmo que muestre el área y perímetro de un círculo
PI = 3.14

print("-- Area de un Cuadrado --")
r = float(input("Radio: "))
print("------- Perimetro -------")

A = round(PI * (r * r))
P = round(2 * PI * r)

print("----------------------")
print("Area: ", A,"cm2")
print("Perimetro: ", P,"cm")
print("----------------------")
