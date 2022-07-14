vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    multa = (vel - 80) * 7 #7 Reais de multa para cada Km acima de 80Km/h
    print('MULTADO! Você excedeu o limite permitido de 80Km/h')
    print('Você deve pagar uma multa de R${}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
