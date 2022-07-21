num = int(input('Digite um número para calcular seu fatorial: '))

count = num 
fat = 0

while count > 0:
    print(count, end='')
    print(' x ' if count > 1 else ' = ', end='')
    mult = num * count
    count -= 1
    fat += mult

print('O valor fatorial de {} é igual a {}'.format(num, fat))