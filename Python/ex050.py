# Pede a entrada de 6 números e soma apenas os pares

soma = 0
cont = 0
contpar = 0

for i in range(1, 7):
    num = int(input('Digite um número para ser somado: '))
    cont += 1
    if num % 2 == 0:
        soma += num
        contpar += 1
print('Foram digitados {} números e a soma dos {} números pares digitados é {}!'.format(cont, contpar, soma))