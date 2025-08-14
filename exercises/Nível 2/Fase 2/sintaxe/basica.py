# Entrada e saída
x = int(input())  # lê um número inteiro
s = input()       # lê string

# Múltiplos valores na mesma linha
a, b = map(int, input().split())

# Estruturas de repetição
for i in range(5):  # 0 até 4
    print(i)

while condicao:
    # repete até condicao ser falsa
    pass

# Condicional
if x > 10:
    print("maior")
elif x == 10:
    print("igual")
else:
    print("menor")

# Listas
lista = [1, 2, 3]
lista.append(4)     # adiciona
lista.sort()        # ordena crescente
lista.sort(reverse=True)  # ordena decrescente
print(len(lista))   # tamanho
