# Crie um programa para mostrar apenas os números ímpares baseando-se na quantidade pedida
i = 1
n = int(input('Digite o valor de n: '))
f = 1

while i <= n:
    f = f * i
    i = i + 1
    
print(f)