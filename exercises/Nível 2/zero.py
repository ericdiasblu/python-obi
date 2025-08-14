n = int(input())

lista = []

for i in range(n):
    x = input()
    if x == '0':
        lista.pop()
    else:
        lista.append(int(x))

total = sum(lista)
print(total)