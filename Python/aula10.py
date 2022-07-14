"""nome = str(input('Qual é o seu nome? '))
if nome == 'Fernando':
    print('Que nome lindo você tem!')
    print('Bom dia, {}!'.format(nome))
else:
    print('Bom dia, apenas.')"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média é {:.1f}'.format(m))
print('Você foi aprovado' if m >= 7 else 'Você foi reprovado')


"""if m >= 7:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')"""
