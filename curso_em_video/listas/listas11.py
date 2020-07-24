"""
    Desafio 088
    Sortear números para a mega sena
    e exibi-los na tela!
"""
import random
import os
lista = list()
print("#="*10, end="")
print("JOGA NA MEGA SENA",end="")
print("#="*10)
num = int(input("Quantos jogos você deseja que eu sorteei? "))
os.system('cls')
print("-="*10,end='')
print("JOGOS SORTEADOS", end="")
print("-="*10)
for cont in range(1,num+1):
    lista = [[random.randint(0,99)],[random.randint(0,99)],[random.randint(0,99)],[random.randint(0,99)],[random.randint(0,99)]]
    print(f"Lista {cont}: {lista}")
print("-="*10, end="")
print("< BOA SORTE >", end="")
print("-="*10)
