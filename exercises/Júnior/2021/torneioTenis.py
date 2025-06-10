jogos = 6
vitorias = 0
derrotas = 0

for i in range(jogos):
    x = input()
    if x == 'V':
        vitorias += 1
    elif x == 'P':
        derrotas += 1

if vitorias >= 5 and vitorias <= 6:
        print('1')
elif vitorias >= 3 and vitorias <= 4:
        print('2')
elif vitorias >= 1 and vitorias <= 2:
        print('3')
elif vitorias == 0:
        print('-1')