# Desenvolvido por: Leonardo Santos da Rocha
# Início do projeto: 11/01/2021 | Fim do projeto: 12/01/2021
# Encontre-me no Linkedin: https://www.linkedin.com/in/leonardo-rocha-a523ab18a/

# Dicionário:
# e = escolha
# a = auxiliar
# f = fim do jogo
# n = número de peças totais
# q = quantidade de peças removidas por jogada
# m = quantidade permitida de peças removidas por jogada

# Enunciado do jogo (OK)
def inicio_nim():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada')
    e = int(input('2 - para jogar um campeonato '))
    print()
    while e != 1 and e != 2:
        print('1 - para jogar uma partida isolada')
        e = int(input('2 - para jogar um campeonato '))
        print()
    return e

# Devolve o número de peças removidas pelo computador (OK)
def computador_escolhe_jogada(n, m):
    # Variáveis
    a = n # Auxiliar igual a quantidade de peças restantes
    # Se quantidade de peças tiradas for menor que peças restantes
    if m < n:
        # Enquanto o resto da estratégia vencedora (n & (m+1)) for diferente de zero
        while (a % (m+1) != 0):
            a -= 1
        q = n - a
    # Se a quantidade de peças tiradas for maior que peças restantes
    else:
        q = n
    # Retornando o valor do resto das peças
    return q

# Devolve o número de peças removidas pelo usuário (OK)
def usuario_escolhe_jogada(n, m):
    q = int(input('Quantas peças você vai tirar? '))
    # Enquanto quantidade removida por jogada por menor que quantidade permitida
    while q <= 0 or q > m or n < m:
        print()
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        q = int(input('Quantas peças você vai tirar? '))
        print()
    return q

# Devolve o modo de jogo campeonato (OK)
def campeonato():
    # Rodadas
    print('**** Rodada 1 ****')
    print()
    partida()
    print('**** Rodada 2 ****')
    print()
    partida()
    print('**** Rodada 3 ****')
    print()
    partida()
    # Final do campeonato
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você 0 X 3 Computador')

# Execução do jogo (OK)
def partida():
    # Escolha das peças, quantidade e limite (OK)
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()

    # Condição de parada do jogo (OK)
    if((n % (m+1) == 0)):
        # Usuário começa a jogar (OK)
        print('Voce começa!')
        print()
        # Enquanto quantidade de peças diferente de zero
        while n != 0:
            # Jogadas do usuário:
            # Quantidade de peças restantes:
            q = usuario_escolhe_jogada(n, m)
            # Restante das peças (número - quantidade):
            n -= q
            # print()
            # Condição para troca de texto
            if q > 1:
                print(f'Você tirou {q} peças.')
            if q == 1:
                print(f'Você tirou uma peça.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n == 0:
                print('Fim do jogo! Você ganhou!')
            print()

            # Jogadas do computador:
            # Quantidade de peças restantes:
            q = computador_escolhe_jogada(n, m)
            # Restante das peças (número - quantidade)
            n -= q
            # Condição para troca de texto
            if q > 1:
                print(f'O computador tirou {q} peças.')
            if q == 1:
                print(f'O computador tirou uma peça.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                print()
                break
            print()

    else:
        # Computador começa a jogar (OK)
        print('Computador começa!')
        print()
        # Enquanto quantidade de peças diferente de zero
        while n != 0:
            # Quantidade de peças restantes:
            q = computador_escolhe_jogada(n, m)
            # Restante das peças (número - quantidade):
            n -= q
            # Condição para troca de texto
            if q > 1:
                print(f'O computador tirou {q} peças.')
            if q == 1:
                print(f'O computador tirou uma peça.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                print()
                break
            print()

            # Jogadas do usuário:
            # Quantidade de peças restantes:
            q = usuario_escolhe_jogada(n, m)
            # Restante das peças (número - quantidade):
            n -= q
            # Condição para troca de texto
            if q > 1:
                print(f'Você tirou {q} peças.')
            if q == 1:
                print(f'Você tirou uma peça.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n == 0:
                print('Fim do jogo! Você ganhou!')
            print()

# Execução do programa (OK)
def main():
    # Variável para selecionar o tipo de jogo (OK)
    e = inicio_nim()
    # Qual o tipo de jogo:
    if e == 1:
        print('Você escolheu uma partida isolada!')
        print()
        partida()
    else:
        print('Você escolheu um campeonato!')
        print()
        campeonato()

main()