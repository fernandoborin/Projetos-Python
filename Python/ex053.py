# Escreve a frase/palavra digitada de trás para frente
# e identifica se ela é um palíndromo

frase = input('Digite uma frase/palavra: ').strip().upper()
print('O inverso de {} é {}'.format(frase, frase[::-1]))

if frase == frase[::-1]:
    palindromo = 'é'
else:
    palindromo = 'não é'

print('A frase/palavra digitada {} um palíndromo!'.format(palindromo))