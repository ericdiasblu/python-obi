p = input()

vogais = ['a', 'e', 'i', 'o', 'u']
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
consoantes = [c for c in alfabeto if c not in vogais]

nova_palavra = ""

for letra in p:
    if letra in vogais:
        nova_palavra += letra
    else:
        # Encontra a vogal mais próxima, com desempate para a que vem primeiro no alfabeto
        menor_dist = float('inf')
        vogal_mais_proxima = ''
        for v in vogais:
            dist = abs(ord(letra) - ord(v))
            if dist < menor_dist or (dist == menor_dist and v < vogal_mais_proxima):
                menor_dist = dist
                vogal_mais_proxima = v

        # Encontra próxima consoante
        idx = consoantes.index(letra)
        if idx < len(consoantes) - 1:
            proxima_consoante = consoantes[idx + 1]
        else:
            proxima_consoante = letra  # se for z

        nova_palavra += letra + vogal_mais_proxima + proxima_consoante

print(nova_palavra)
