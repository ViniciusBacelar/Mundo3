"""
    Desafio 090
    Programa que lê nome e média
    de um aluno, guardando também 
    a situação em um dicionário.
    No final, mostre o conteúdo da
    estrutura na tela.
"""
import os
while True:
    escola = list()
    aluno = dict()
    aluno["nome"] = str(input("Qual seu nome? "))
    aluno["nota1"] = float(input("Qual sua primeira nota? "))
    aluno["nota2"] = float(input("Qual sua segunda nota? "))
    aluno["nota3"] = float(input("Qual sua terceira nota? "))
    aluno["media"] = (aluno["nota1"]+aluno["nota2"]+aluno["nota3"])/3
    if (aluno["media"] >= 7):
        aluno["status"] = "Aprovado!"
    else:
        aluno["status"] = "Reprovado!"
    escola.append(aluno)
    os.system("cls")
    print("=="*30)
    print(f'Aluno = {escola[0]["nome"]}')
    print(f'Media das notas = {escola[0]["media"]}')
    print(f'Status do aluno = {escola[0]["status"]}')
    print("=="*30)
    esc = str(input("Deseja continuar? [S/N] "))
    if esc not in("Ss"):
        break