# Soma os valores entre 1 e 500 que são ímpares e múltiplos por 3

cont = 0
n = 0

for i in range(1, 501): 
    if i % 3 == 0 and i % 2 != 0: # % 3 =0 0 faz com que sejam múltiplos e
        n = n + i                 # % 2 != 0 com que sejam ímpares
        cont = cont + 1

print('A soma entre os {} valores que são divisíveis por 3 é de {}'.format(cont, n))