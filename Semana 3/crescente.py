# Crie um programa para verificar a ordenação dos números
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if(a < b and b < c):
    print('crescente')
else:
    print('não está em ordem crescente')