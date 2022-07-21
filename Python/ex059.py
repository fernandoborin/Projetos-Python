# Lê dois números e pede uma ação a ser feita com eles

from time import sleep

print('=-' * 10)
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
usr = 0

while usr != 5:
    sleep(1)
    print('=-' * 15)
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    print('=-' * 15)

    usr = int(input('Qual é a sua opção? '))
    sleep(1)
    if usr == 1:
        print('O resultado de {} + {} é {}'.format(valor1, valor2, valor1 + valor2))
    elif usr == 2:
        print('O resultado de {} x {} é {}'.format(valor1, valor2, valor1 * valor2))
    elif usr == 3:
        if valor1 > valor2:
            maiorvalor = valor1
        else:
            maiorvalor = valor2
        print('Entre {} e {} o maior valor é {}'.format(valor1, valor2, maiorvalor))
    elif usr == 4:
        print('Informe os valores novamente')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))

print('Finalizando...')
sleep(1)
print('~' * 15)