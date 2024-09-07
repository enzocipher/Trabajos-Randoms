import math
ResultadoFinal = 0; eleccion = input("ingrese 1 o 2"); n=int(input("ingrese cantidad w"))
if eleccion == '1': a = 45.23
if eleccion == '2': a = 56.22 
for i in range(1, n+1):
    if (i%2 == 0):
        siesnegativo = -1
    else: siesnegativo = 1
    ResultadoFinal += siesnegativo*((a*i)/(math.factorial(i)))
print(ResultadoFinal)
