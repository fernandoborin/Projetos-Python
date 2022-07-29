# Usa while para produzir uma PA com o primeiro termo e razão, com
# a opção de contar mais termos após os 10 primeiros

count = 0
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

while count < 10:
    print(termo, end= '')
    print(' -> ' if count < 9 else ' ', end='')
    termo += razao
    count += 1

count = 0
print('')
count2 = int(input('Quantos termos você quer mostrar a mais? '))

while count < count2:
    print(termo, end= '')
    print(' -> ' if count < (count2 - 1) else ' ', end='')
    termo += razao
    count += 1
    if count == count2:
        print('')
        escolha = input('Quer continuar? [S/N]: ').upper()
        if escolha == 'S':
            count2 = int(input('Quantos termos você quer mostrar a mais? '))
            count = 0

print('----- FIM -----')