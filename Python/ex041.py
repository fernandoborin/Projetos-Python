from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade > 25:
    categoria = 'MASTER'
elif idade > 19:
    categoria = 'SÊNIOR'
elif idade > 14:
    categoria = 'JUNIOR'
elif idade > 9:
    categoria = 'INFANTIL'
else:
    categoria = 'MIRIM'
print('Classificação: {}'.format(categoria))