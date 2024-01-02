#Algoritmo que muestra el porcentaje de alumnos aprobados y desaprobados.

print("-- MOSTRAR EL PORCENTAJE DE ALUMNOS APROBADOS Y DESAPROBADOS --")
print("Ingrese cantidad de alumnos aprobados: ")
alumnosAp = int(input(":)"))

print("Ingrese cantidad de alumnos desaprobados: ")
alumnosDes = int(input(":)"))

pA = (alumnosAp * 100) / (alumnosAp + alumnosDes)
pD = (alumnosDes * 100) / (alumnosAp + alumnosDes)


print("Aprobados ", (round(pA * 100)/ 100), "%")
print("Desaprobados ", (round(pD * 100)/ 100), "%")
