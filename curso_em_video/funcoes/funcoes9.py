"""
    Desafio 104
    Programa que cria um loop e lê um valor
    se o valor for um número ele verificará 
    e retornará a confirmação e encerrará o
    loop, caso não seja, o loop irá continuar
    até que um número seja digitado.
"""
def lerNum(num = 0):
    """[Função que verifica se o parâmetro é um valor
    númerico ou não. Retornando a confirmação ou uma negação]

    Args:
        num (int, optional): [Parâmetro que será verificado]. Defaults to 0.

    Returns:
        [str]: [Resultado da verificação]
    """
    if(num.isnumeric()):
        return f"Você acabou de digitar um número! o {num}"        
    else:
        return "ERRO! Tente novamente!"
    
def main():
    """
    [Função principal]
    """
    valor = 0
    while True:
        num = input("Digite um número: ")
        print(lerNum(num))
        if(num.isnumeric()):
            valor = True
            if valor:
                break
    help(lerNum)
main()