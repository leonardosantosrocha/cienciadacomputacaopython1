# Crie um programa para ler o fatorial de N números digitados pelo usuário
n = int(input('Digite o número: '))
while n > 0:
    f = 1
    while n > 1:
        f *= n
        n -= 1
    print(f)
    n = int(input('Digite o número: '))
    