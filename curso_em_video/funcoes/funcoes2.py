"""
    Desafio 097
    Programa que leia e alinhe
    por meio de uma função e de modo
    dinâmico qualquer frase.
"""
import os 
def escreva(txt):
    print("="*len(txt))
    print(txt)
    print("="*len(txt))

def main():    
    x = str(input("Digite algo ou uma frase: "))
    os.system('cls')
    escreva(x)
    
main()