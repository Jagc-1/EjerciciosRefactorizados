#Algoritmo que calcula el total de ventas realizadas por hombres y mujeres de N empleados.

tv_h = 0
tv_m = 0
muj = 0


print("Ingrese la Cantidad de empleados: ")
empleados = int(input(":)"))

for cont in range(1, empleados + 1):
    print("Empleado Nro", cont, "/", empleados)
    print("Nombre: ")
    nombre = str(input(":)")).lower()
    print("Genero (H/M): ")
    genero = str(input(":)")).upper()
    print("Ventas: ")
    ventas = int(input(":)"))

    if genero == "H":
        tv_h += ventas
    elif genero == "M":
        tv_m += ventas
        muj += 1

print("Total Ventas Hombres: ", tv_h)
print("Total Ventas Mujeres: ", tv_m)
print("----------------------------")
print("Porcentaje Venta Mujeres: ", (muj * 100)/empleados, "%" )
print("----------------------------")
