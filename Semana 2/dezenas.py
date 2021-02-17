# Criando um programa para identificar o algarismo da dezena dos números
x = int(input('Digite um número inteiro: '))
x = x // 10
x = x % 10
print(f'O dígito das dezenas é {x}')
