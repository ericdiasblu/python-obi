min_cafe = int(input())
max_cafe = int(input())
capacidade = int(input())
dose = int(input())

atende_cliente = False
for qtd_doses in range(capacidade // dose + 1):
    total_cafe = qtd_doses * dose
    restante = capacidade - total_cafe
    if min_cafe <= restante <= max_cafe:
        atende_cliente = True
        break

print("S" if atende_cliente else "N")