# Crie uma função para calcular o fatorial
def fatorial(x):
    i = 0
    f = 1
    while i < x:
        f = f * (x - i)
        i += 1
    return f

# Crie uma função para calcular o binomio de newton
def binomial(n, k):
    return (fatorial(n)) / (fatorial(k) * (fatorial(n-k)))

# Retornando a função fatorial
print(fatorial(5))
# Retornando a função binomial
print(binomial(5, 3))