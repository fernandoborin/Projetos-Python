casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual é o seu salário mensal? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
valorparcela = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {:.0f} anos,'.format(casa, anos), end='')
print(' a prestação mensal será de R${:.2f}'.format(valorparcela))
if valorparcela > (salario * 0.30):
    print('Empréstimo NEGADO!')
elif valorparcela <= (salario * 0.30):
    print('Empréstimo APROVADO')


#Valor da casa, salário e em quantos anos vai pagar
#A prestação não pode exceder 30% do salário