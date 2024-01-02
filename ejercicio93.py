#Algoritmo que muestre el nombre completo de un programa al ingresar su primera letra.


print('Letra [V - P - C - J - F]')
letra = str(input(':)')).upper()

if letra == 'V':
    print('Visual Basic')
elif letra == 'P':
    print('Pascal')
elif letra == 'C':
    print('C#')
elif letra == 'J':
    print('Java')
elif letra == 'F':
    print('Fortran')
else:
    print('Opcion invalida')
