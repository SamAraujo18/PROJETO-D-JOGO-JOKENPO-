from time import sleep
import random
#LISTA DAS RESPOSTAS DO BOT (0/1)
lista = ['Pedra','Papel','Tesoura']

#MENU DO JOGO
print('-=-' * 20)
nome = str(input('Digite seu nome para prosseguir: '))
print('-=-' * 20)
print(f'Olá \033[1;96m{nome}\033[m seja bem vindo ao jogo do Jokenpô\033[1;97m v1.0\033[m')
print('-=-' * 20), sleep(3)
print("""Logo abaixo mostraremos o menu do jogo:

          [1] \033[1;97mIniciar\033[m
          [2] \033[1;97mCreditos\033[m""")
print('')
sleep(0.1)
e1 = input('Digite alguma opção para continuar: ')
print('')
#MENU ALTERNATIVO '1'
if e1 == '1':
    print('\033[0;97n-=-\033[m' * 25)
    print('\033[0;36mProcessando...\033[m')
    print('-=-' * 25), sleep(3.7)
    print("""\033[1;91m    OBS: PARA VOCÊ JOGAR VOCÊ DEVE TENTAR UTILIZAR UM DOS TRÊS COMANDOS PARA PODER DUELAR CONTRA A MAQUINA
          SEGUINDO A LOGICA QUE VOCÊ DEVE TENTAR GANHAR DA MAQUINA UTILIZANDO OS SEGUINTES COMANDOS:
          
                                     \033[1;97mPEDRA, PAPEL E TESOURA\033[m.
                                     
          \033[1;91mCOM ISSO VOCÊ TERÁ QUE TENTAR UTILIZAR ESSES COMANDOS ATÉ TENTAR GANHAR DA MAQUINA.\033[m""")
    print('-=-' * 25), sleep(6)
    print(' ')
    input('\033[4;97mPRESSIONE ENTER PARA CONTINUAR PARA O JOGO:\033[m ').strip()
    print(' ')
    print('-=-' * 25)
    print('\033[1;95mJogo iniciado:\033[m ')
    print('')
    print("""          \033[1;97m[0] PEDRA\033[m
          \033[1;97m[1] PAPEL\033[m
          \033[1;97m[2] TESOURA\033[m""")
    print('')
    r1 = input('Digite qual é a sua jogada: ').upper()
    print('')
    sleep(0.1)
    respostadobot = (random.choice(lista))
    print('-=-' * 15)
    print(' '), sleep(1)
    print('JO'), sleep(1.1)
    print('KEN'), sleep(1.2)
    print('PO!!!'), sleep(1)
    print('-=-' * 10)
    print(f'Computador jogou {respostadobot}')
    print(f'Jogador jogou {r1}'.replace('0', 'Pedra').replace('1', 'Papel').replace('2', 'Tesoura'))
    print('-=-' * 10)
    if respostadobot == 'Pedra' and r1 == '2':
        print(f'HAHAHA! EU COLOQUEI "\033[1;93m{respostadobot}\033[m" PORTANTO EU VENCI :) ')
    if respostadobot == 'Tesoura' and r1 == '1':
        print(f'HAHAHA! EU COLOQUEI "\033[1;93m{respostadobot}\033[m" PORTANTO EU VENCI :) ')
    if respostadobot == 'Papel' and r1 == '0':
        print(f'HAHAHA! EU COLOQUEI "\033[1;93m{respostadobot}\033[m" PORTANTO EU VENCI :) ')
    if respostadobot == 'Pedra' and r1 == '0':
        print('\033[1;91mEMPATAMOS!\033[m PORÉM, DA PRÓXIMA VEZ IREI GANHAR DE VOCÊ!!')
    if respostadobot == 'Papel' and r1 == '1':
        print('\033[1;91mEMPATAMOS!\033[m PORÉM, DA PRÓXIMA VEZ IREI GANHAR DE VOCÊ!!')
    if respostadobot == 'Tesoura' and r1 == '2':
        print('\033[1;91mEMPATAMOS!\033[m PORÉM, DA PRÓXIMA VEZ IREI GANHAR DE VOCÊ!!')
    if respostadobot == 'Tesoura' and r1 == '0':
        print('PARABÉNS!! VOCÊ GANHOU DE MIM NO JOKENPÔ!')
        print('')
        print('\033[1;97mFIM DO JOGO!\033[m \033[0;91m(O JOGO AINDA ESTÁ EM DESENVOLVIMENTO, AGUARDE ATUALIZAÇÕES)\033[m')
    if respostadobot == 'Papel' and r1 == '2':
        print('PARABÉNS!! VOCÊ GANHOU DE MIM NO JOKENPÔ!')
        print('')
        print('\033[1;97mFIM DO JOGO!\033[m \033[0;91m(O JOGO AINDA ESTÁ EM DESENVOLVIMENTO, AGUARDE ATUALIZAÇÕES)\033[m')
    if respostadobot == 'Pedra' and r1 == '1':
        print('PARABÉNS!! VOCÊ GANHOU DE MIM NO JOKENPÔ!')
        print('')
        print('\033[1;97mFIM DO JOGO!\033[m \033[0;91m(O JOGO AINDA ESTÁ EM DESENVOLVIMENTO, AGUARDE ATUALIZAÇÕES)\033[m')


#MENU ALTERNATIVO '2'
if e1 == '2':
    sleep(1)
    print('-=-' * 20)
    print()
    print('\033[1;97m             Desenvolvedor do Jogo: \033[1;36mCrowZek\033[m')
    print()
    print('-=-' * 20)
    sleep(1)
    input('\nDigite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
    print(' ')
    print('-=-' * 20)
    print('\033[1;93mProcessando...\033[m'), sleep(2.5)
    print('-=-' * 20)
    print(' ')
# OUTRO MENU ALTERNATIVO (2)
    print("""Voltamos ao menu do jogo:

          [1] \033[1;97mIniciar\033[m
    
          """)
    e1 = input('Digite alguma opção para continuar: ')
    print('')
    if e1 == '1':
        print('\033[0;97n-=-\033[m' * 25)
        print('\033[0;36mProcessando...\033[m')
        print('-=-' * 25), sleep(3.7)
        print("""\033[1;91m    OBS: PARA VOCÊ JOGAR VOCÊ DEVE TENTAR UTILIZAR UM DOS TRÊS COMANDOS PARA PODER DUELAR CONTRA A MAQUINA
              SEGUINDO A LOGICA QUE VOCÊ DEVE TENTAR GANHAR DA MAQUINA UTILIZANDO OS SEGUINTES COMANDOS:
              
                                         \033[1;97mPEDRA, PAPEL E TESOURA\033[m.

              \033[1;91mCOM ISSO VOCÊ TERÁ QUE TENTAR UTILIZAR ESSES COMANDOS ATÉ TENTAR GANHAR DA MAQUINA.\033[m""")
        print('-=-' * 25), sleep(6)
        print(' ')
        input('\033[4;97mPRESSIONE ENTER PARA CONTINUAR PARA O JOGO:\033[m ').strip()
        print(' ')
        print('-=-' * 25)
        print('\033[1;95mJogo iniciado:\033[m ')
        print('')
        r1 = input('Digite qual é a sua jogada: ').upper()
        print('')
        sleep(0.1)
        respostadobot = (random.choice(lista))
        print('-=-' * 15)
        print(' '), sleep(1)
        print('JO'), sleep(1.1)
        print('KEN'), sleep(1.2)
        print('PO!!!'), sleep(1)
        print('-=-' * 10)
        print(f'Computador jogou {respostadobot}')
        print(f'Jogador jogou {r1}'.replace('0', 'Pedra').replace('1', 'Papel').replace('2', 'Tesoura'))
        print('-=-' * 10)
        if respostadobot == 'Pedra' and r1 == '2':
            print(f'HAHAHA! EU COLOQUEI "\033[1;93m{respostadobot}\033[m" PORTANTO EU VENCI :) ')
        if respostadobot == 'Tesoura' and r1 == '1':
            print(f'HAHAHA! EU COLOQUEI "\033[1;93m{respostadobot}\033[m" PORTANTO EU VENCI :) ')
        if respostadobot == 'Papel' and r1 == '0':
            print(f'HAHAHA! EU COLOQUEI "\033[1;93m{respostadobot}\033[m" PORTANTO EU VENCI :) ')
        if respostadobot == 'Pedra' and r1 == '0':
            print('\033[1;91mEMPATAMOS!\033[m PORÉM, DA PRÓXIMA VEZ IREI GANHAR DE VOCÊ!!')
        if respostadobot == 'Papel' and r1 == '1':
            print('\033[1;91mEMPATAMOS!\033[m PORÉM, DA PRÓXIMA VEZ IREI GANHAR DE VOCÊ!!')
        if respostadobot == 'Tesoura' and r1 == '2':
            print('\033[1;91mEMPATAMOS!\033[m PORÉM, DA PRÓXIMA VEZ IREI GANHAR DE VOCÊ!!')
        if respostadobot == 'Tesoura' and r1 == '0':
            print('PARABÉNS!! VOCÊ GANHOU DE MIM NO JOKENPÔ!')
            print('')
            print(
                '\033[1;97mFIM DO JOGO!\033[m \033[0;91m(O JOGO AINDA ESTÁ EM DESENVOLVIMENTO, AGUARDE ATUALIZAÇÕES)\033[m')
        if respostadobot == 'Papel' and r1 == '2':
            print('PARABÉNS!! VOCÊ GANHOU DE MIM NO JOKENPÔ!')
            print('')
            print(
                '\033[1;97mFIM DO JOGO!\033[m \033[0;91m(O JOGO AINDA ESTÁ EM DESENVOLVIMENTO, AGUARDE ATUALIZAÇÕES)\033[m')
        if respostadobot == 'Pedra' and r1 == '1':
            print('PARABÉNS!! VOCÊ GANHOU DE MIM NO JOKENPÔ!')
            print('')
            print(
                '\033[1;97mFIM DO JOGO!\033[m \033[0;91m(O JOGO AINDA ESTÁ EM DESENVOLVIMENTO, AGUARDE ATUALIZAÇÕES)\033[m')
