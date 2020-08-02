def lerInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Erro de tipos.")
            continue
        except KeyboardInterrupt:
            print("Usuário preferiu não digitar esse número.")
            return 0
        else:
            return n
def lerFloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Erro de tipos.")
            continue
        except KeyboardInterrupt:
            print("Usuário preferiu não digitar esse número.")
            return 0
        else:
            return n
def main():
    num = lerInt("Digite um valor: ")
    num2 = lerFloat("Digite um valor: ")
    print(f"O valores digitados: {num} e {num2}")
    
main()