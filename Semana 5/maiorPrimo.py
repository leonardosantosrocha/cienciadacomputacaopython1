# Crie um programa para retornar o maior número primo possível
def checa_primo(n):
    i = 2
    resto = 1

    if n == 0 and n == 1:
        print('não primo')
    else:
        while i < n and resto != 0:
            resto = n % i
            i += 1
        
    if resto != 0:
        return True
    else:
        return False

def maior_primo(n):
    if checa_primo(n) == True:
        return n
    else:
        while checa_primo(n) == False:
            n -= 1
        return n