import numpy as np
# 1. Criando uma matriz com valores pequenos
A = np.array([[1.0000001, 2.0000002], [3.0000003, 4.0000004]])
B = np.array([[1, 2], [3, 4]])

# 2. Verificando se as matriz são exatamente iguais
print("Matriz A")
print(A)
print("\nMatriz B:")
print(B)
print("\nSão exatamente iguais?")
print(np.array_equal(A, B)) # Compara se são idênticas

# 3. Comaparação com tolerância
tolerance = 1e-7
print("\nComparação considerando erro numérico:")
print(np.allclose(A, B, atol=tolerance)) # Permite uma margem de erro

# 4. Analisando os erros numéricos
differences = np.abs(A - B)
print("\nMatriz de diferenças:")
print(differences)