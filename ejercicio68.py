#Algoritmo que calcule el salario a pagar de un trabajador.
sueldoBAse = 0
numHijos = 0
diasNoLAb = 0
sueldoFinal = 0

print("-- CALCULAR EL SUELDO FINAL DE UN EMPLEADO --")
print("Ingese sueldo Base: $")
sueldoBAse = int(input(":)"))

print("Ingrese numero de hijos: ")
numHijos = int(input(":)"))

print("Ingrese le numro de dias no laborados")
diasNoLAb = int(input(":)"))

sueldoFinal = sueldoBAse + (numHijos * 100) + (diasNoLAb * 25)

print("Sueldo Final :$", sueldoFinal)
