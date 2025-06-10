# Tipos de Dados

inteiro = 5         # int
decimal = 3.14      # float
texto = "Oi"        # str
lista = [1, 2, 3]   # list

# Entrada e Saída de Dados

nome = input()

idade = int(input())

print("oi",nome)

# Condicionais
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")

# Laços de Repetição (for)

for i in range(5):  # 0 até 4
    print(i)

for i in range(1, 6):  # 1 até 5
    print(i)

# Laços de Repetição (while)

x = 0
while x < 5:
    print(x)
    x += 1

# Listas

numeros = [10, 20, 30]
print(numeros[0])       # 10
numeros.append(40)      # Adiciona no final
print(len(numeros))     # Tamanho da lista

# Funções

def soma(a, b):
    return a + b

print(soma(3, 4))  # 7
