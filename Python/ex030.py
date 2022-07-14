n = int(input('Digite um número: '))
div = n % 2 #Qualquer número que se dividido por 2 restar 0 é par, do contrário é impar
print('O número {} é PAR'.format(n) if div == 0 else 'O número {} é IMPAR'.format(n))
