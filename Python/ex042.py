print('~' * 34)
print('Analisador de triângulos foda 2.0')
print('~' * 34)
print('')
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 != l2 == l3 or l2 != l1 == l3 or l3 != l1 == l2:
        print('ISÓSCELES!')
    elif l1 != l2 != l3:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
