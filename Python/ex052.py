# Testa se o número digitado é primo

num = int(input('Digite um número: '))
div = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        div += 1
    else:
        print('\033[31m', end='')
    print(i, end=' ')

print('O número {} foi divisível {} vezes'.format(num, div))

if div == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')