from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador escolher um número
print('-' * 60)
print('Hmm, vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 60)
num = int(input('Em que número eu pensei? ')) #Jogador escolhe um número
print('PROCESSANDO...')
sleep(2)
if num == computador:
    print('Parabéns, você acertou!')
else:
    print('Você errou, eu pensei no número {}, não {}!'.format(computador, num))