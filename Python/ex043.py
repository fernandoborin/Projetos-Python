peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura * altura) #A altura ao quadrado também poderia ser calculada com altura ** 2
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso ideal!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Cuidado, você está em OBESIDADE MÓRBIDA!')
