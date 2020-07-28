"""
    Desafio 095
    Programa do desafio 093 aprimorado
"""
lista = []
while True:
    dic = {"Nome":str(input('Qual o nome do jogador? ')).strip().capitalize(),
           "Partidas":int(input('Quantas partidas jogadas? '))}

    dic["Gols"] = sum([int(input(f'Quantos gols na partida {i}? ')) for i in range(1, dic["Partidas"]+1)])

    dic["Média"] = float(dic["Gols"]/dic["Partidas"])

    lista += [dic]

    flag = str(input('\nContinuar? (S/N) ')).strip().lower()[0]
    if flag == 'n':
        break

while True:
    select = str(input('\nDeseja ver os dados de qual jogador? \n'
                       '(Para sair, digite "sair")')).strip().capitalize()
    if select == 'Sair':
        break

    i = 0
    while lista[i]["Nome"] not in select:  ## Você 'obriga' o programa a loopar até achar a lista em que está o nome.
        i += 1
        if i == len(lista)-1 and lista[i]["Nome"] not in select:
            print('Não há jogador com esse nome')
            i = 0
            select = str(input('\nDeseja ver os dados de qual jogador? \n'
                               '(Para sair, digite "sair")')).strip().capitalize()

    if lista[i]["Nome"] == select:
        print('='*10, 'RESULTADO', '='*10)
        print(f'Nome: {lista[i]["Nome"]}'
              f'\nNúmero de partidas: {lista[i]["Partidas"]}'
              f'\nNúmero total de gols: {lista[i]["Gols"]}'
              f'\nMédia de gols por partida: {lista[i]["Média"]:.2f}')