try:
    numero = int(input("Digite um número inteiro: "))

    match (numero > 0, numero % 2 == 0):
        case (True, True):
            print("O número é positivo e par.")
        case (True, False):
            print("O número é positivo e impar.")
        case (False, True) if numero != 0:
            print("O número é negativo e par.")
        case (False, False) if numero != 0:
            print("O número é negativo e ímpar.")
        case _:
            print("O número é zero.")
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")