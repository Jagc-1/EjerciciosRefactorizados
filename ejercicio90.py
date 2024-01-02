#Algoritmo que muestre las cuatro operaciones básicas.


print('-- Bienvenido, aqui sabras que las cuatro operaciones básicas son --')
print('1. Suma')
print('2. Resta')
print('3. Multiplicación')
print('4. División')
print('------------------------')

print('Seleccione una opción: ')
opcion = int(input(':)'))

if opcion == 1:
    print('Ingrese el primer número: ')
    numero1 = int(input())
    print('Ingrese el segundo número: ')
    numero2 = int(input())
    print('La suma es: ', numero1 + numero2)
elif opcion == 2:
    print('Ingrese el primer número: ')
    numero1 = int(input())
    print('Ingrese el segundo número: ')
    numero2 = int(input())
    print('La resta es: ', numero1 - numero2)
elif opcion == 3:
    print('Ingrese el primer número: ')
    numero1 = int(input())
    print('Ingrese el segundo número: ')
    numero2 = int(input())
    print('La multiplicación es: ', numero1 * numero2)
elif opcion == 4:
    print('Ingrese el primer número: ')
    numero1 = int(input())
    print('Ingrese el segundo número: ')
    numero2 = int(input())
    print('La división es: ', numero1 // numero2)
else:
    print('Opcion invalida, ingrese una opcion que si lo sea')
