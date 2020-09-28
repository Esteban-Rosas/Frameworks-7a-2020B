#Script: Number race
#Esteban Rosas - Darwin Martinez
'''
    Description:
    randint: Let me generate integer numbers
    uniform: Let me generate float numbers
'''
import os
from random import randint
#Functions:::::::::::::::::::::::::::::
def dices () :
    d1 = randint(1,6)
    d2 = randint(1,6)
    tot = d1 + d2
    return [d1, d2, tot]

#Main::::::::::::::::::::::::::::::::::
sumaT = []
cont_par = 0
cont_impar = 0
os.system("cls")
numero = int(input("ingresar valor: "))
i = 1
if numero>=1:
    while i <= numero :
        print("Tiro Nro: ", i)
        dd = dices()
        sumaT.append(dd[2])
        print("d1: ", dd[0])
        print("d2: ", dd[1])
        print("Total: ",dd[2])
        i = i + 1
#=============Pares e Impares=============
        if dd[2] % 2 == 0:
            cont_pares +=1
        else:
            cont_impares += 1
#=============Finalizar=============
        if dd[0] & dd[1]==6:
            break
        key = input("::: Lanzar nuevamente :::")

    print("La suma total es: ", sum(sumaT))
    print("Total numeros pares es: ", cont_pares)
    print("Total numeros impares es: ", cont_impares)

else:
    print("Valor minimo es 1.")
