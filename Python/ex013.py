f = float(input('Qual é o salário do funcionário? R$'))
d = float(input('Qual é a porcentagem de aumento no salário? '))
print('O funcionário que recebia R${:.2f}, com um aumento de {}%, passará a receber R${:.2f}'.format(f, d, f + f * d / 100))
