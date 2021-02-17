# Crie um programa para procurar um cartão de crédito em uma lista de cartões
meuCartao = int(input('Digite o número do seu cartão de crédito: '))
cartaoAuxiliar = 1
encontreiMeuCartao = False

while cartaoAuxiliar != 0 and not encontreiMeuCartao:
    cartaoLido = int(input('Digite o número do próximo cartão de crédito: '))
    if cartaoLido == meuCartao:
        encontreiMeuCartao = True

if encontreiMeuCartao:
    print('Cartão encontrado!')
else:
    print('Cartão não encontrado!')