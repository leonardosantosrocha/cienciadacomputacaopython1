n = int(input('Digite um número inteiro maior que um: '))
fator = 2
multiplicidade = 0

while n > 1:
    while(n % fator == 0):
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print(f'Fator {fator} multiplicidade = {multiplicidade}')
    fator = fator + 1
    multiplicidade = 0