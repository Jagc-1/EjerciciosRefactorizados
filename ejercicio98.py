# Algoritmo que muestra el área, base y altura de un triángulo.


print('-- MENU DE OPCIONES DE TRIANGULO --')
print('1.  Área de un trtiangulo dada la base y altura')
print('2. Base del triangulo dada la altura y el área')
print('3. Altura de un triangulo dada la base y área')

print('Escoja una....')
opcion = int(input(':)'))

if opcion == 1:
    base = float(input('Ingrese la base: '))
    altura = float(input('Ingrese la altura: '))
    area = base * altura/2
    print(f'El área del triángulo es: {area:.2f}')

elif opcion == 2:
    altura = float(input('Ingrese la altura: '))
    area = float(input('Ingrese el área: '))
    base = (area * 2)/altura
    print(f'La base del triángulo es: {base:.2f}')

elif opcion == 3:
    base = float(input('Ingrese la base: '))
    area = float(input('Ingrese el área: '))
    altura = (area * 2)/base
    print(f'La altura del triángulo es: {altura:.2f}')
else:
    print('Opción incorrecta')
