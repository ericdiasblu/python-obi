escola = int(input())
supermercado = int(input())
lojinha = int(input())

rota1 = abs(escola - lojinha) + abs(lojinha - supermercado) + abs(supermercado - escola)
rota2 = abs(escola - supermercado) + abs(supermercado - lojinha) + abs(lojinha - escola)

print(min(rota1, rota2))