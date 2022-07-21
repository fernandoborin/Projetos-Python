from random import randint 

cont = 1
comnum = randint(0, 10)

print('-' * 54)
print('COMPUTADOR: Acabei de pensar em um número entre 0 e 10')
print('será que você consegue adivinhar qual foi?')
print('')

usrnum = int(input('Qual o seu palpite? '))

while usrnum != comnum:
    if usrnum < comnum:
        print('Mais... Tente novamente')
    if usrnum > comnum:
        print('Menos... Tente novamente')
    
    usrnum = int(input('Qual o seu palpite? '))

    cont += 1

print('Eu escolhi o número {}, você acertou com {} tentativas. Parabéns!'.format(comnum, cont))