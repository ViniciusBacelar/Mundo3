"""
    Desafio 081
    Programa que lê 5 valores e os cadastra em
    uma lista, os ordena de modo reverso e diz
    se o numero 5 faz parte ou nao.
"""
cont = 0
valores = list()
while(True):
    n = int(input("Digite um valor: "))
    cont = cont + 1
    print("Valor adicionado com sucesso...")
    r = str(input("Quer continuar? [S/N]"))
    if r in ('Nn'):
        break

if(cont == 1):
    print("-="*30)
    print(" ")
    print(f'Foi digitado apenas {1} numero, o {valores[0]}')
    print("Impossivel ordenar apenas um numero!")
    if 5 not in valores:
        print("O 5 não foi digitado")
    else:
        print("O 5 faz parte dessa lista!")
    print(" ")
    print("-="*30)
else:
    print("-="*30)
    print(" ")
    print(f'Foram digitados {cont} numeros')
    valores.sort(reverse=True)
    print(f"Valores digitados em modo decrescente: {valores}")
    if 5 not in valores:
        print("O 5 não faz parte dessa lista!")
    else:
        print("O 5 faz parte dessa lista!")
    print(" ")
    print("-="*30)
