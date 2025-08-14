n = int(input())
L = list(map(int, input().split()))

i = 0
j = n - 1
operacoes = 0

while i < j:
    if L[i] == L[j]:
        i += 1
        j -= 1
    elif L[i] < L[j]:
        L[i + 1] += L[i]
        i += 1
        operacoes += 1
    else:
        L[j - 1] += L[j]
        j -= 1
        operacoes += 1

print(operacoes)