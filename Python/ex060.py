# Faz o fatorial do número digitado sem utilizar a função math.factorial

num = int(input('Digite um número para calcular seu fatorial: '))

count = num 
fat = 1

while count > 0:
    print(count, end='')
    print(' x ' if count > 1 else ' = ', end='')
    fat *= count
    count -= 1
print(fat)
print('O valor de {}! é igual a {}'.format(num, fat))