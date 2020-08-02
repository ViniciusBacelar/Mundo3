import moedas
import os
import lin
preco = float(input("Digite um preço: "))
taxa = float(input("Digite uma taxa: "))
os.system('cls')
lin.lin()
print(f"Metade de {preco}: {moedas.dividir(preco, True)}R$")
lin.lin()
print(f"Dobro de {preco}: {moedas.dobrar(preco, True)}R$")
lin.lin()
print(f"Aumentar {taxa}% de {preco}R$: {moedas.aumentar(preco,taxa, True)}R$")
lin.lin()
print(f"Reduzir {taxa}% de {preco}R$: {moedas.reduzir(preco,taxa, True)}R$")
lin.lin()









