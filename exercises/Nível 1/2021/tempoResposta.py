registros = int(input())
tempo = 0

for i in range(registros):
    caracter, contato = input().split()
    contato = int(contato)
    tempo+1

print(contato," ",tempo)