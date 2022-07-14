d = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos Km foram rodados? '))
aluguel = d * 60
preço = km * 0.15
total = aluguel + preço
print('O aluguel do carro totalizou R${:.2f}'.format(aluguel))
print('O preço pela distância rodada é de R${:.2f}'.format(preço))
print('O total a pagar é de R${:.2f}'.format(total))
