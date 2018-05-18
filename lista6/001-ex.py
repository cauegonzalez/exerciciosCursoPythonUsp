def computador_escolhe_jogada(n, m):
    i = 1
    print('')
    while ((i >= 1) and i <= m):
        if ((n - i) % (m + 1)) == 0:
            if (i == 1):
                print('O computador tirou uma peça.')
            else:
                print('O computador tirou {} peças.'.format(i))
            return i
        i = i + 1
    if (i == m):
        if (m == 1):
            print('O computador tirou uma peça.')
        else:
            print('O computador tirou {} peças.'.format(m))
        return m

def usuario_escolhe_jogada(n, m):
    print('')
    escolha = int(input('Quantas peças você vai tirar? '))
    while ((escolha <= 0) or (escolha > m)):
        print('')
        print('Oops! Jogada inválida! Tente de novo.')
        print('')
        escolha = int(input('Quantas peças você vai tirar? '))
        print('')

    if (escolha == 1):
        print('Você tirou uma peça.')
    else:
        print('Você tirou {} peças.'.format(escolha))
    return (escolha)

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print('')

    if ((n % (m + 1)) == 0):
        print('Você começa!')
        while n > 0:
            retirada = usuario_escolhe_jogada(n, m)
            n = n - retirada
            if (n > 0):
                if (n == 1):
                    print('Agora resta apenas uma peça no tabuleiro.')
                else:
                    print('Agora restam {} peças no tabuleiro.'.format(n))
            if (n == 0):
                print('Fim do jogo! Você ganhou!')
                return 0
            else:
                retirada = computador_escolhe_jogada(n, m)
                n = n - retirada
                if (n > 0):
                    if (n == 1):
                        print('Agora resta apenas uma peça no tabuleiro.')
                    else:
                        print('Agora restam {} peças no tabuleiro.'.format(n))

                if (n == 0):
                    print('Fim do jogo! O computador ganhou!')
                    return 1
    else:
        print('Computador começa!')
        while n > 0:
            retirada = computador_escolhe_jogada(n, m)
            n = n - retirada
            if (n > 0):
                if (n == 1):
                    print('Agora resta apenas uma peça no tabuleiro.')
                else:
                    print('Agora restam {} peças no tabuleiro.'.format(n))

            if (n == 0):
                print('Fim do jogo! O computador ganhou!')
                return 1
            else:
                retirada = usuario_escolhe_jogada(n, m)
                n = n - retirada
                if (n > 0):
                    if (n == 1):
                        print('Agora resta apenas uma peça no tabuleiro.')
                    else:
                        print('Agora restam {} peças no tabuleiro.'.format(n))
                if (n == 0):
                    print('Fim do jogo! Você ganhou!')
                    return 0

def campeonato():
    i = 1
    placarComputador = 0
    placarUsuario = 0
    ganhador = 0
    while (i <= 3):
        print('')
        print('**** Rodada {} ****'.format(i))
        print('')
        ganhador = partida()
        if (ganhador == 1):
            placarComputador = placarComputador + 1
        else:
            placarUsuario = placarUsuario + 1
        i = i + 1
    print('')
    print('**** Final do campeonato! ****')
    print('')
    print("Placar: Você {} X {} Computador".format(placarUsuario, placarComputador))
    print('')

    if (placarComputador > placarUsuario):
        return 1
    return 0

def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    opcao = int(input('2 - para jogar um campeonato '))

    if (opcao == 1):
        print('')
        print('Você escolheu uma partida!')
        partida()
    else:
        print('')
        print('Você escolheu um campeonato!')
        campeonato()

main()