"""
    Desafio 079
    Programa que lê vários valores númericos
    e os cadastram em uma lista. Caso, o número
    já exista, ele não será adicionado, ao fim
    todos os valores digitados irão aparecer em
    ordem crescente. 
"""
valores = list()
while(True):
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print('Valor duplicado! Não irei adicionar....')
    r = str(input("Quer continuar? [S/N]"))
    if r in ('Nn'):
        break
    
valores.sort()    
print("-="*30)
print(" ")
print(valores)
print(" ")
print("-="*30)