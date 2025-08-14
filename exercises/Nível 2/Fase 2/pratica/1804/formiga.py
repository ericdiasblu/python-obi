saloes, tuneis, partida = map(int, input().split())

while True:
    alturas = list(map(int, input().split()))
    if len(alturas) == saloes:
        break

for i in range(tuneis):
    i, j = map(int, input().split())

