# Escreve a frase/palavra digitada de trás para frente
# e identifica se ela é um palíndromo

frase = input('Digite uma frase/palavra: ').strip().upper() # Converte a string em
#print('O inverso de {} é {}'.format(frase, frase[::-1]))   # letras maiúsculas

palavras = frase.split()  # Separa a frase em uma lista de palavras
junto = ''.join(palavras) # Remove os espaços entre as palavras
inverso = ''

for letra in range(len(junto) - 1, -1, -1): # Usando a função for 
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    palindromo = 'é'
else:
    palindromo = 'não é'

"""if frase == frase[::-1]: # [::-1] faz a string ser escrita de trás pra frente
    palindromo = 'é'
else:
    palindromo = 'não é'"""

print('A frase/palavra digitada {} um palíndromo!'.format(palindromo))