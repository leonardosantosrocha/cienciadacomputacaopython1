# Crie um programa para verificar se um número é divisível por três e cinco
x = int(input('Digite um número: '))

if(x % 3 == 0 and x % 5 == 0):
    print('FizzBuzz')
else:
    print(x)