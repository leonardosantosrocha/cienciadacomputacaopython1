# Crie um programa que some os algarismos de um número
n = int(input("Digite um número inteiro: "))
soma = 0

while n:
    soma = soma + n % 10 # Pegando o último número e atribuindo a soma
    n = n // 10 # Retirando o último algarismo

print(soma)