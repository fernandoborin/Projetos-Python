# Faz o valor fatorial de N

print('-' * 50)
print()

n = int(input('Digite o número que quer descobrir o fatorial: '))
oldn = n
print()

for i in range(1, n - 1):
    n = n * (i + 1) 

print('O valor fatorial de {} é igual a {}'.format(oldn, n))