"""
    Desafio 101
    Ler anos de nascimento e dizer
    Se com base nos anos lidos, é
    obrigatório votar, opcional ou
    se é negado o direito de votar.
"""
def voto(ano = 0):
    """[Função que irá receber o ano de nascimento
    e diminuir do ano corrente, armazenando o resultado
    dentro da variavel 'status'. Passando em seguida por
    uma estrutura de repetição que irá retornar a um valor
    para o estado indicao 
    ]

    Args:
        ano (int, optional): [Ano de nascimento]. Defaults to 0.

    Returns:
        [int]: [Retorno da estrutura condicional]
    """
    from datetime import date
    data = date.today().year
    global status
    status = data - ano
    if(status >= 18):
        return 1
    elif(status>=16) and(status<18):
        return 2
    else:
        return 3
    
def main():
    """[Função principal]
    """
    nascimento = int(input("Ano de nascimento: "))
    if voto(nascimento) == 1:
        print(f'Voto obrigatório!, você possui {status} anos de idade!')
    elif voto(nascimento) == 2:
        print(f'Voto opcional!, você possui {status} anos de idade!')
    else:
        print(f'Negado!, você possui {status} anos de idade!')
        
main()