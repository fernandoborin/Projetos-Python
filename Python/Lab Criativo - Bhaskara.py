# Faz o delta e as raízes de uma equação de segundo grau

print('-' * 26)
print()
a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))
print()

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('A equação não possui raízes reais, pois o delta é menor que 0.')
else:
    print('O delta de {}, {} e {} é: {}'.format(a, b, c, delta))
    print()
    bhaskara1 = (-b + delta ** 0.5) / (2 * a)
    bhaskara2 = (-b - delta ** 0.5) / (2 * a)
    print('As duas raizes da equação são x1 = {:.0f} e x2 = {:.0f}'.format(bhaskara1, bhaskara2))
    print()
