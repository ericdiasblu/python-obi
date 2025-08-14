s = int(input())      # Lê o valor alvo da soma dos algarismos
a = int(input())      # Lê o início do intervalo
b = input()           # Lê o fim do intervalo (deveria ser int, veja observação abaixo)

count = 0             # Inicializa o contador de números que satisfazem a condição

for i in range(a, b+1):   # Para cada número de a até b (inclusive)
    algarismos = [int(d) for d in str(i)]  # Separa os algarismos do número i
    if sum(algarismos) == s:               # Se a soma dos algarismos for igual a s
        count += 1                         # Incrementa o contador

print(count)           # Exibe o total encontrado