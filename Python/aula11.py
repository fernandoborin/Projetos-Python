#a = 3
#b = 5
#print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = input('Digite seu nome: ')
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['vermelho'], nome, cores['limpa']))