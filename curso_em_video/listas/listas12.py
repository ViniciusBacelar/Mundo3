"""
    Desafio 089
    Armazenar nome e snotas de alunos
    , calcular a media deles e mostrar
    na tela.
"""
while(True):
    lista = list()
    nome = str(input("Nome: "))
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    media = (nota1 + nota2)/2
    lista.append([nome,[nota1,nota2], media])
    esc = str(input("Quer continuar? [S/N]"))
     
    if esc not in ("Ss"):
        break
    
    print("-="*30)
    print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
    print("-="*30)
    for i, a in enumerate(lista):
        print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    while True:
         print("-="*30)
         opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
         if opc == 999:
             print("FINALIZANDO...")
             break
         if opc <=len(lista) - 1:
             print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
    print("<<<< Volte sempre! >>>>")