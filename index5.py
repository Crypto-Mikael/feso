import numpy as np

# Criando um vetor (array unidimensional)
vetor = np.array([1, 2, 3, 4, 5])
print("Vetor:")
print(vetor)

# Criando um matriz 2x3 (duas linhas, tres colunas)
matriz = np.array([[1, 2, 3], [4, 5, 6]]);
print("\nMatriz 2x3:")
print(matriz)

# Acessando elementos
print("\nElemento do vetor na posicao (1,2):", vetor[1])
print("\nElemento da matriz na posicao (1,2):", matriz[0, 1])

# Operacoes basicas
print("\n Soma do vetor: ", np.sum(vetor))
print("Soma dos elementos da matriz: ", np.sum(matriz))

# Transposta da matriz
print("\nMatriz Transposta:")
print(matriz.T)
