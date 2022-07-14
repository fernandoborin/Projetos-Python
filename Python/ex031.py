d = float(input('Digite a distância em Km da viagem: '))
print('Você está prestes a começar uma viagem de \033[34m{}Km\033[m.'.format(d))
v = d * 0.45 if d > 200 else d * 0.50
"""if d > 200:
    v = d * 0.45
else:
    v = d * 0.50"""
print('O preço da sua passagem será de \033[34mR${:.2f}\033[m!'.format(v))
