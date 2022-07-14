salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario * 1.15 if salario <= 1250 else salario * 1.10
print('Quem ganhava \033[33mR${:.2f}\033[m agora passará a ganhar \033[33mR${:.2f}\033[m!'.format(salario, aumento))
