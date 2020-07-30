"""
    Desafio 103
    Leia o nome do jogador e a quantidade de gols
    feitos durante o campeonato e os exiba no retorno da função.
"""

def jogador(nome="Desconhecido", gols="Desconhecido"):
    """
    [Função que recebe o nome do jogador e o número de gols
    e retorna uma frase concatenada exibindo os mesmos.]

    Args:
        nome (str, optional): [Nome do jogador]. Defaults to "Desconhecido".
        gols (str, optional): [Quantidade de gols]. Defaults to "Desconhecido".
    """
    return(f'O jogador {nome} fez {gols} gols no campeonato!')


def main():
    """
    [Função principal]
    """
    import os
    nome = str(input("Nome do jogador: "))
    gols = int(input("Gols no campeonato: "))
    os.system('cls')
    print(jogador(nome, gols))
    
main()