# Crie um programa para informar números adjacentes
n = int(input('Digite um número inteiro: '))
tamanho = len(str(n))

while tamanho > 1:
    ultimo = n % 10 # ultimo
    n = n // 10 # restante do número
    penultimo = n % 10 # penultimo vale o restante
    if ultimo == penultimo:
        tamanho = 0 # sai do laço
    else:
        tamanho = len(str(n)) # altera o tamanho de n

if tamanho == 0:
    print('sim')
else:
    print('não')