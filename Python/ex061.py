# Conta os 10 primeiros valores de uma PA usando a função while

count = 0
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

while count < 10:
    print(termo, end= ' -> ')
    termo += razao
    count += 1

print('FIM')