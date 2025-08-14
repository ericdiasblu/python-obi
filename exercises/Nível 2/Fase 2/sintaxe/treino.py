# 4️⃣ Questões-treino rápidas para hoje

# Soma simples
# Leia 2 inteiros e imprima a soma
a, b = map(int, input().split())
print(a + b)

# Maior número
# Leia N, depois N números, imprima o maior
n = int(input())
nums = list(map(int, input().split()))
print(max(nums))

# Contagem de pares
# Leia N e depois N números, conte quantos são pares
n = int(input())
nums = list(map(int, input().split()))
pares = sum(1 for x in nums if x % 2 == 0)
print(pares)

# Inverter ordem
# Leia N números e imprima em ordem inversa
nums = list(map(int, input().split()))
print(*nums[::-1])
