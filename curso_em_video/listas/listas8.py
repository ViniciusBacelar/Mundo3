"""
    Desafio 085
    Crie um programa que leia 
    sete valores numericos e
    cadastre-os em uma lista 
    separada, no final mostre 
    os valores juntos e em ordem
    crescente.
"""
import os
pares = list()
div = list()
nDiv = list()
impares = list()
total = list()
cont = 1
for x in range(0, 7):
    par = int(input(f"Digite o {cont}o numero par: "))
    if (par % 2 == 0):
        pares.append(par)
    else:
        while(True):    
            print("O numero precisa ser par!")
            par = int(input(f"Digite o {cont}o numero par: "))
            if( par % 2 == 0):
                break
    impar = int(input(f"Digite o {cont}o numero impar: "))
    if (impar % 2 != 0):
        impares.append(impar)
    else:
        while(True):    
            print("O numero precisa ser impar!")
            impar = int(input(f"Digite o {cont}o numero impar: "))
            if( impar % 2 != 0):
                break
    total.append(pares[:])
    div.append(pares[:])
    total.append(impares[:])
    nDiv.append(impares[:])
    cont += 1
    pares.clear()
    impares.clear()
total.sort()
nDiv.sort()
div.sort()
os.system("cls")
print("=-"*30)
print("")
print(f"Pares em ordem crescente: {div}")
print(f'Impares em ordem crescente: {nDiv}')
print(f'Numeros digitados em ordem crescente: {total}')
print("")
print("=-"*30)