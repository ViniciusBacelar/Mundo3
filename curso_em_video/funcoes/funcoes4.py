"""
    Desafio 099
    programa que tenha uma função
    chamada maior(), que receba vários 
    parâmetros com valores inteiros.
    O programa deve analisar todos e dizer
    qual o maior valor.
"""
def lin():
    print("=="*30)
def maior():
    lista = list()
    while True:
        x = int(input("Digite um numero: "))
        lista.append(x)
        esc = str(input("Deseja continuar? [S/N] "))
        if esc not in "Ss":
            lin()
            print()
            print(f"Foram informados {len(lista)} numeros")
            print()
            
            lista.sort()
            lin()
            print()
            print(f"Numeros digitados em ordem crescente: {lista}")
            print()
            
            lista.sort(reverse=True)
            lin()
            print()
            print(f"Numeros digitados em ordem decrescente: {lista}")
            print()
            
            maxnum = max(lista)
            minnum = min(lista)
            lin()
            print()
            print(f"Menor numero: {minnum}")
            print()
            lin()
            print()
            print(f"Maior numero: {maxnum}")
            print()
            lin()
            
            break
        
maior()