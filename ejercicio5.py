#Muestra la Serie Fibonacci. 0,1,1,2,3,5,8,13,21,34

A = 0
B = 1
C = 0


for cont in range(10):
    print("-------------------")
    print(cont, ":", A)
    C = A + B
    A = B
    B = C
