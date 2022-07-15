# Calculadora simples utilizando a função for

n = int(input('Digite um número para ver sua tabuada: '))

#for i in range(1, 11):
#    r = n * i 
#    print('{} x {} = {}'.format(n, i, r))

for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n * i))