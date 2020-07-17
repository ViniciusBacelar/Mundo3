x = int(input("Digite um numero de 0 a 20: "))
numeros = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
           "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"]
while ((x < 0) or (x > 20)):
    print(f'Numero {x} invalido, tente novamente e digite outro!')
    x = int(input("Digite um numero de 1 a 20: "))
if ((x >= 0) and (x <= 20)):
    print(f'==== Voce digitou: {numeros[x]} ====')
