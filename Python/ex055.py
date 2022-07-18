# Utiliza for para ler uma lista de pesos e informar o maior e menor valor 

pesoslista = []

for pessoa in range(1, 6):
    pesos = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    pesoslista.append(pesos) # Adiciona a entrada de valores a lista

pesoslista.sort() # Organiza os valores em ordem crescente

print('O menor peso lido foi: {}'.format(pesoslista[0])) # Printam respectivamente o primeiro
print('O maior peso lido foi: {}'.format(pesoslista[4])) # e último valor da lista