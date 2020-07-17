"""
    Desafio 082
    Programa que lê 5 valores e os cadastra em
    uma lista, e mostra quais sao pares e impares
"""
impares = list()
pares = list()
valores = list()
while(True):
    n = int(input("Digite um valor: "))
    valores.append(n)
    print("Valor adicionado com sucesso...")
    if (n % 2 == 0):
        pares.append(n)
    else:
        impares.append(n)
    r = str(input("Quer continuar? [S/N]"))
    if r in ('Nn'):
        break

print("-="*30)
print(" ")
print(f'Valores digitados: {valores}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
print(" ")
print("-="*30)
