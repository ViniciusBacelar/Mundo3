lanche = ("hamburguer","lasanha","pizza","suco")
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')

print("==== Fim da primeira forma ====")

x = 0

for comida in lanche:
    print(f'Eu vou comer {comida} na posicao {x}')
    x = x + 1

print("==== Fim da segunda forma ====")

for pos, food in enumerate(lanche):
    print(f'Eu vou comer {food} na posicao {pos}')


print("==== Fim da terceira forma ====")

print("==== FIM DO PROGRAMA ====")
