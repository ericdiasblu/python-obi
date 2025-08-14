# 2️⃣ Funções & truques que ajudam MUITO na OBI

# Entrada rápida
import sys
input = sys.stdin.readline  # deixa a entrada mais rápida

# Lista de números a partir de uma linha
nums = list(map(int, input().split()))

# Ordenação rápida
nums.sort()         # in-place
ordenada = sorted(nums)  # retorna nova lista

nums.sort(reverse=True)

# Mínimo e máximo
menor = min(nums)
maior = max(nums)

# Soma de elementos
total = sum(nums)

# Percorrer índices e valores ao mesmo tempo
for i, val in enumerate(nums):
    print(i, val)

# Contar frequência de itens
from collections import Counter
contagem = Counter(nums)
print(contagem[5])  # quantas vezes o 5 aparece

# Fatiamento de listas
print(nums[1:4])  # do índice 1 até o 3
print(nums[::-1]) # inverte lista

# Grafo
S = 4
grafo = [[] for _ in range(S + 1)]
grafo[1].append(2)  # liga 1 -> 2
grafo[2].append(3)  # liga 2 -> 3

#dfs
visitado = [False] * (S + 1)

def dfs(no):
    visitado[no] = True
    for viz in grafo[no]:
        if not visitado[viz]:
            dfs(viz)
