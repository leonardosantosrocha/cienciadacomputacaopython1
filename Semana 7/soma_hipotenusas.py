# Crie um programa para verificar a soma de hipotenusas
def calcular_hipotenusa(ca, co):
    return ((ca ** 2) + (co ** 2))

def soma_hipotenusas(n):
    i = 1
    soma = 0
    while (i <= n):
        h = (i*i)       
        ca = 1
        co = 1
        while (ca < n):
            while (co < n):
                if (h == calcular_hipotenusa(ca, co)):
                    soma = soma + i
                    ca = n
                    break
                co += 1
            ca += 1
            co = ca
        i += 1
  
    return soma

print(soma_hipotenusas(25))