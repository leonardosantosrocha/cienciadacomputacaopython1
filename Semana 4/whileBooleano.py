# Crie um programa para verificar ordens decrescentes
decrescente = True
anterior = int(input('Digite o primeiro número da sequência: '))
valor = 1

while valor != 0 and decrescente:
    valor = int(input('Digite o próximo número da sequência: '))
    if valor > anterior:
        decrescente = False
    else:
        anterior = valor

if decrescente == True:
    print('A sequência está em ordem decrescente!')
else:
    print('A sequência não está em ordem decrescente!')