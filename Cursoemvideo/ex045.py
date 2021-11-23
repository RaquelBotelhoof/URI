from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')

if computador == 0:  # pedra
    if jogador == 0:
        print('Jogo empatado')
    elif jogador == 1:
        print('Jogador ganhou')
    elif jogador == 2:
        print('Computador ganhou')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  # papel
    if jogador == 0:
        print('Comutador ganhou')
    elif jogador == 1:
        print('Jogo empatado')
    elif jogador == 2:
        print('Computador ganhou')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # tesoura
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Jogo empatado')
    else:
        print('JOGADA INVÁLIDA')
