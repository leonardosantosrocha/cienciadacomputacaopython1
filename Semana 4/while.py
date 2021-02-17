# Laço para imprimir as potências de dois
i = 0
while i <= 10:
    print(2 ** i)
    i = i + 1

print()

# Laço para realizar diversas somas até parar o laço digitando zero
valor = 1
soma = 0
while valor != 0:
    valor = int(input('Digite um inteiro a ser somado: '))
    soma = soma + valor
print(f'A soma dos valores digitados é: {soma}')

print()

# Laço para realizar somas baseadas nas vezes escolhidas pelo usuário
repeticoes = int(input('Quantos repetições o laço terá: '))
valor = 0
soma = 0
i = 0
while i < repeticoes:
    valor = int(input('Digite um inteiro a ser somado: '))
    soma = soma + valor
    i = i + 1
print(f'A soma dos valores digitados é: {soma}')