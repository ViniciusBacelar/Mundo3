try:
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    result = num1 / num2
except (ValueError, TypeError):
    print(f"Erro encontrado nos tipos digitados")
except KeyboardInterrupt:
    print(f"O usuário não informou os dados")
except ZeroDivisionError:
    print(f"Impossível dividir {num1} por 0.")
except Exception as erro:
    print(f"Erro: {erro}")
else:
    print(f'Programa leu os tipos corretos')
    print(f'Valor da divisão:{result:.0f}')
finally:
    print("Fim do programa!")