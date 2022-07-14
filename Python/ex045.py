from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('~' * 12)
print('Jokenpo Foda')
print('~' * 12)
print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('')
sleep(0.5)
print('-~' * 12)
sleep(0.5)
print('Computador jogou {}'.format(itens[computador]))
print('')
sleep(0.5)
print('Jogador jogou {}'.format(itens[jogador]))
sleep(0.5)
print('-~' * 12)
print('')
sleep(0.5)

if computador == 0: # Pedra
    if jogador == 0:
        print('EMPATE')
    if jogador == 1:
        print('JOGADOR VENCE')
    if jogador == 2:
        print('COMPUTADOR VENCE')

elif computador == 1: # Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('JOGADOR GANHA')

elif computador == 2: # Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    if jogador == 1:
        print('COMPUTADOR VENCE')
    if jogador == 2:
        print('EMPATE')
