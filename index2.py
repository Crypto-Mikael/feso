# Simulando a leitura de um valor digitado pelo usuário
valor_lido = 0.1 + 0.2 # O usuário esperava que fosse

# Valor esperado
valor_esperado = 0.3

# Exibindo os valores
print(f"Valor lido: {valor_lido}")
print(f"Valor esperado: {valor_esperado}")

# Verificando se os valores são iguais
print("\nOs valores são exatamente iguais?")
print(valor_lido == valor_esperado) # Deveria se True, ,as pode ser False

# Diferença causada pelo erro numérico
print("\nErro numérico:")
print(abs(valor_lido - valor_esperado))

# Soulução: Comparação com tolerância
tolerancia = 1e-10
print("\nComparação com tolerância: ")
print(abs(valor_lido - valor_esperado) < tolerancia)

