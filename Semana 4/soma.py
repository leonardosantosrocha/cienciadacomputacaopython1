# Crie um programa pra realizar a soma de vários números
soma = 0
valor = 1
while valor != 0:
    valor = int(input('Digite um valor a ser somado: '))
    soma = soma + valor

print(f'A soma dos valores digitados é: {soma}')
