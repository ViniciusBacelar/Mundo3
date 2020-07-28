"""
    Desafio 098
    Programa que chama uma função
    contador()  e realiza o calculo
    de 10 a 1, de 0 a 10 e outro cálculo
    com números personalizados.
"""
import os 
def lin():
    print("=="*30)
def contador():
    lin()
    def dez():
        for x in range(0, 10):
            x += 1
            print(x,end="  ")
    dez() 
    print("FIM!")
    lin()
    print()
    
    def zero():
        y = 10
        for cont in range(0,5):
            y -= 2
            print(y,end="  ")
            cont += 1
    
    zero()
    print("FIM!")
    print()
    
    def person(p1,p2,p3):
        lin()
        print()
        while(p1<=p3):
            p1 += p2
            if p1 > p3:
                p1 -= p2
                break
            print(p1,end="  ")
        print("FIM!")
        print()
        lin()
        
    lin()
    x1 = int(input("Digite o inicio: "))
    x2 = int(input("Digite o passo: "))
    if(x2 == 0):
        x2 = 1
    x3 = int(input("Digite o fim: "))
    if(x3 == 0):
        x3 = x1 * 5
    lin()
    os.system('cls')
    person(x1,x2,x3)

def main():
    contador()

main()
                      