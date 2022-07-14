p = float(input('Qual o preço do produto? R$'))
d = float(input('Qual a porcentagem do desconto? '))
print('O produto custa R${:.2f}. Com {}% de desconto, custará R${:.2f}.'.format(p, d, p - (p * d / 100)))
