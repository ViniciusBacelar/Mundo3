"""
    Desafio 087
    Criar matriz 3x3
    mostrando ao fim 
    a soma de todos os valores digitados
    a soma dos valores da terceira coluna
    o maior valor da segunda coluna
"""
matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
cont = 0
lista = list()
for l in range(0,3):
        for c in range(0,3):
                matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
                if (matriz[l][c] % 2 == 0):
                    spar = spar + matriz[l][c]
                if (c == 2):
                    scol = scol + matriz[l][c]
                
print("-="*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end=' ')
        print()
        
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
    
print(f"Soma dos números pares: {spar}")
print(f"Soma dos valores da teceira coluna: {scol}")
print(f"Maior valor da linha 2: {mai}")
