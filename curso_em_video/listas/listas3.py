"""
    Desafio 080
    Programa que lê 5 valores e os cadastra em
    uma lista, ordenadamente.
"""
import os
lista = list()
while(True):
    def listas3():
        i = 0
        lista.append(int(input("Digite um valor: ")))
        print(f'{lista[i]} foi adicionado ao final da lista, na posicao: {i}')
        i = i + 1
        if(i == 1):
            x = int(input("Digite o segundo valor: "))
            if (x >= lista[0]):
                lista.append(x)
                lista.sort()
                print(f'O {x} foi adicionado na posição: {i}, ', end=" ")
                print(f'Depois do {lista[i-1]}')
                i = i + 1
            else:
                lista.append(lista[0])
                lista[0] = x
                print(f'O {x} foi adicionado na posição: 0, ', end="")
                print(f'Antes do {lista[1]} na  posição: 1')
                i = i + 1
        if(i == 2):
            x = int(input("Digite o terceiro valor: "))
            if (x >= max(lista)):
                lista.append(x)
                lista.sort()
                print(f'O {x} foi adicionado na posição: {i}, ', end=" ")
                print(f'Depois do {lista[i-1]}')
                i = i + 1
            elif(x <= min(lista)):
                lista.append(lista[0])
                lista.sort()
                lista[0] = x
                print(f'O {x} foi adicionado na posição: 0, ',end=" ")
                print(f'Antes do {lista[1]}, na posição: 1')
                i = i + 1
            else:
                lista.append(x)
                lista.sort()
                for c, y in enumerate(lista):
                    if(x == y):
                        print(f'O {y} foi adicionado na posição: {c}, ', end='')
                        print(f'Uma posição depois do {lista[c-1]} e ', end='')
                        print(f'uma posição antes do {lista[c+1]}.')
                        i = i + 1
        if(i == 3):
            x = int(input("Digite o quarto valor: "))
            if (x >= max(lista)):
                lista.append(x)
                lista.sort()
                print(f'O {x} foi adicionado na posição: {i}, ', end=" ")
                print(f'Depois do {lista[i-1]}')
                i = i + 1
            elif(x <= min(lista)):
                lista.append(lista[0])
                lista.sort()
                lista[0] = x
                print(f'O {x} foi adicionado na posição: 0, ',end=" ")
                print(f'Antes do {lista[1]}, na posição: 1')
                i = i + 1
            else:
                lista.append(x)
                lista.sort()
                for c, y in enumerate(lista):
                    if(x == y):
                        print(f'O {y} foi adicionado na posição: {c}, ', end='')
                        print(f'Uma posição depois do {lista[c-1]} e ', end='')
                        print(f'uma posição antes do {lista[c+1]}.')
                        i = i + 1
        if(i == 4):
            x = int(input("Digite o quinto valor: "))
            if (x >= max(lista)):
                lista.append(x)
                lista.sort()
                print(f'O {x} foi adicionado na posição: {i}, ', end=" ")
                print(f'Depois do {lista[i-1]}')
                i = i + 1
            elif(x <= min(lista)):
                lista.append(lista[0])
                lista.sort()
                lista[0] = x
                print(f'O {x} foi adicionado na posição: 0, ',end=" ")
                print(f'Antes do {lista[1]}, na posição: 1')
                i = i + 1
            else:
                lista.append(x)
                lista.sort()
                for c, y in enumerate(lista):
                    if(x == y):
                        print(f'O {y} foi adicionado na posição: {c}, ', end='')
                        print(f'Uma posição depois do {lista[c-1]} e ', end='')
                        print(f'uma posição antes do {lista[c+1]}.')
                        i = i + 1
        os.system('cls')
        print("=-"*30)
        print(" ")
        print(f'Sequência de valores colocados no array, de modo ordenado: {lista}')
        print(" ")
        print("=-"*30)
    listas3()
    break
