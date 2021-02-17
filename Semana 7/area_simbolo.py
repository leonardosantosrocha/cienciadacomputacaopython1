# Crie um programa para calcular a área e prenchê-la com hashtags
def area():
    i = j = 1
    largura = int(input('digite a largura: '))
    altura = int(input('digite a altura: '))
    while i <= largura:
        while j <= altura:
            print(largura * '#')
            j += 1
        i += 1
    
area()