print('-=' * 15)
print(' Analisador de triângulos foda')
print('-=' * 15)
a = float(input('\033[31mPrimeiro segmento: '))
b = float(input('\033[33mSegundo segmento: '))
c = float(input('\033[34mTerceiro segmento: \033[m'))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Os segmentos \033[31m{}\033[m, \033[33m{}\033[m e \033[34m{}\033[m PODEM formar um triângulo!'.format(a, b, c))
else:
    print('Os segmentos {}, {} e {} NÃO PODEM formar um triângulo.'.format(a, b, c))
