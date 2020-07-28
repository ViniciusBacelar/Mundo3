"""
    Desafio 093
    Programa que lê e gerencia
    o aproveitamento de um jogador de futebol
    com base em seu número de partidas
    e da quantidade de seus gols, durante o
    campeonato.
"""
import os

while True:
    jogador = dict()
    jogador['nome'] =  str(input("Digite seu nome: "))
    jogador['partidas'] =  int(input("Digite o numero de partidas que disputou: "))
    golsMax = 0
    partidas = dict()
    x = 1
    for cont in range(0, jogador['partidas']):
        gols = int(input(f"Quantos gols marcou na partida {x}? "))
        partidas[f"partida {x}"] = gols
        x = x + 1
        golsMax = golsMax + gols   
    os.system('cls')
    print("=-"*30)
    print()
    for k,v in partidas.items():
        print(f"{k} {jogador['nome']} marcou {v}")
    jogador['gols'] = golsMax
    jogador['aproveitamento'] = jogador['gols']/jogador['partidas']   
    print()
    print("=-"*30)
    print()
    for k,v in jogador.items():
        print(f"O campo {k}  tem valor {v}")
    print()
    print("=-"*30)
    break
