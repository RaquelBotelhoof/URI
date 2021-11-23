from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-'*20)
jogador = int(input('Em qual número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você acertou, me VENCEU!! Parabéns')
else:
    print('Eu VENCI. O número era {} '.format(computador))


