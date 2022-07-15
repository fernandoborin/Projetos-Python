# Conta os 10 primeiros valores de uma PA usando o termo e razão fornecidos

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for pa in range(0, 9):
    termo += razao
    print(termo, end= ' ')