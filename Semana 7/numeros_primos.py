# Crie um programa para definir se um número é primo
def primos(n):
    i = 2
    resto = 1
    
    if n == 0 and n == 1:
        return 'não primo'
    else:
        while i < n and resto != 0:
            resto = n % i
            i += 1 
    
    if resto != 0:
        return 'primo'
    else:
        return 'não primo'

def numeros_primos():
    n = int(input('Digite um número inteiro: '))
    while n > 0:
        if primos(n) == 'primo':
            print(f'{n} é primo!')
        else:
            print(f'{n} não é primo!')
        n = int(input('Digite um número inteiro: '))

numeros_primos()