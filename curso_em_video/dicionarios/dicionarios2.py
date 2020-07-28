"""
    Desafio 091
    Sorteei valores de um dado
    fictício para quatro jogadores
    e mostre quem tirou o numero maior
    e a ordem dos numeros tirados em ordem.
"""

import random
lista = list()
jogadores = dict()

jogadores["jogador 1"] = random.randint(1,6)
jogadores["jogador 2"] = random.randint(1,6)
jogadores["jogador 3"] = random.randint(1,6)
jogadores["jogador 4"] = random.randint(1,6)

lista = jogadores.copy()

print(lista)
sortedDict = sorted(jogadores.values(), reverse=True)
print(f"Valores ordenados:{sortedDict}")
if (jogadores["jogador 1"] >=jogadores["jogador 2"] ) and (jogadores["jogador 1"] >= jogadores["jogador 3"]) and (jogadores["jogador 1"] >= jogadores["jogador 4"]):
    print(f'Maior valor: {jogadores["jogador 1"]}, pertencente ao jogador 1')
if(jogadores["jogador 2"] >=jogadores["jogador 1"] ) and (jogadores["jogador 2"] >= jogadores["jogador 3"]) and (jogadores["jogador 2"] >= jogadores["jogador 4"]):
    print(f'Maior valor: {jogadores["jogador 2"]}, pertencente ao jogador 2')
if(jogadores["jogador 3"] >=jogadores["jogador 1"] ) and (jogadores["jogador 3"] >= jogadores["jogador 2"]) and (jogadores["jogador 3"] >= jogadores["jogador 4"]):
    print(f'Maior valor: {jogadores["jogador 3"]}, pertencente ao jogador 3')
if(jogadores["jogador 4"] >=jogadores["jogador 1"] ) and (jogadores["jogador 4"] >= jogadores["jogador 2"]) and (jogadores["jogador 4"] >= jogadores["jogador 3"]):
    print(f'Maior valor: {jogadores["jogador 4"]},  pertencente ao jogador 4')
