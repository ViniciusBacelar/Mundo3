"""
    Desafio 078
    Programa que lê 5 valores
    e retorna quais desses valores
    são os maiores e os menores.
    Bônus: Adicionei uma estrutura
    para retornar a posição destes 
    valores também.
"""
lista = []

for cont in range(0, 4):
    lista.append(int(input("Digite um valor: ")))
maxValue = max(lista)
minValue = min(lista)

for c, v in enumerate(lista):
    if (maxValue == v):
        print("="*40)
        print(f' Maior valor: {v} ,', end='')
        print(f' Posição do maior valor: {c}')
        print("="*40)
    if(minValue == v):
        print("="*40)
        print(f' Menor valor: {v} ,', end='')
        print(f' Posição do menor valor: {c}')
        print("="*40)
