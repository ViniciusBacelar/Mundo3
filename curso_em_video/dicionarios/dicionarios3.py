"""
    Desafio 092
    Crie um programa que leia seus dados
    e armazene um dicionario, imprimindo e acrescentando
    valores específicos.
"""
import os
from datetime import date

data_atual = date.today()
ano = data_atual.year
while True: 
    trabalhador = dict()
    trabalhador['nome'] =  str(input("Digite seu nome: "))
    idade =  int(input("Digite seu ano de nascimento: "))
    trabalhador['idade'] = ano - idade
    trabalhador['ctps'] = int(input("Digite seu ctps: [0 encerra] "))
    if (trabalhador['ctps'] == 0):
         for k, v in trabalhador.items():
            os.system('cls')
            print(f"{k} tem valor {v}")
            break
    trabalhador['ano'] = int(input("Digite seu ano de contratação: "))
    trabalhador['salario'] =  int(input("Digite o valor do seu salario: "))
    trabalhador['aposentadoria'] = (trabalhador['ano'] - ano) + 35 + trabalhador['idade']
    os.system('cls')
    for k, v in trabalhador.items():
        print(f"{k} tem valor {v}")
    break
        
