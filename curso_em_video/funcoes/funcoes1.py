"""
    Desafio 096
    Programa com função chamada area()
    que recebe as dimensões de um terreno 
    retangular(largura e comprimento) e mostra
    a area do terreno.
"""
import os
def lin():
    print("=="*30)
def area(largura, comprimento):
    lin()
    area = largura * comprimento
    print(f"A largura {largura}cm e o comprimento {comprimento}cm...")
    lin()
    print(f"Formam uma area de {area}cm2")
    lin()
def main():
    x = float(input("Digite a largura: "))
    y = float(input("Digite o comprimento: "))
    os.system('cls')
    area(x, y)
    
main()
    