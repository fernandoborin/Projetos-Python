# Faz a soma de X elevado a Y termos por Y vezes

print('-' * 25)
print()

x = int(input('Digite um valor para X: '))
y = int(input('Digite o número de termos: '))
print()

exp = y
somaf = 0 

for i in range(0, exp):
    soma = x ** exp
    somaf = somaf + soma
    exp = exp - 1
somaf = somaf + 1

print('A soma de 1 + {} + {}² + {}³... para {} termos é igual a: {}'.format(x, x, x, y, somaf))
