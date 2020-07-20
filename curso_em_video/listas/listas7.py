"""
    Desafio 084
    Programa que leia nome e peso
    de algumas pessoas, armazene 
    numa lista e mostre no final
    o maximo de pessoas cadastradas, 
    o maior peso e o menor peso
"""

result = list()
pesos = list()
cont = 0
while(True):
    lista = []
    nome = str(input("Digite seu nome: "))
    peso = str(input("Digite seu peso: "))
    lista.append(nome)
    lista.append(peso)
    pesos.append(peso)
    cont += 1
    result.append(lista[:])
    
    esc = str(input("Deseja continuar? [S/N]"))
    if esc in ('Nn'):
        break
print("-="*30)
print('')
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi de {max(pesos)}KG')
print(f'O menor peso foi de {min(pesos)}KG')
print('')
print("-="*30)
