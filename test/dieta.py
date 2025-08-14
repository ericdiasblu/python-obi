n, m = map(int, input().split())

lista = []

for i in range(n):
    p, g, c = map(int, input().split())
    calorias_p = p * 4
    calorias_g = g * 9
    calorias_c = c * 4
    lista.append((calorias_p, calorias_g, calorias_c))

calorias_total = sum(calorias_p + calorias_g + calorias_c for calorias_p, calorias_g, calorias_c in lista)

print(m-calorias_total)