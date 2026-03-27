try:
    idade = int(input("Digite sua idade: "))
    carteirinha = input("Digite se voce possui carteirinha de estudante:")

    match (idade <= 5 or idade >= 60, carteirinha == "S"):
        case (True, True):
            print("Passagem gratuita")
        case (True, False):
            print("Passagem gratuita")
        case (False, True):
            print("Passagem meia")
        case (False, False):
            print("Passagem inteira")
        case _:
            print("Passagem inteira")
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")