nome = input('Digite seu nome: ').strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
nome1 = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome1[0], len(nome1[0])))
#O comando nome.find abaixo conta quantos caracteres vieram antes do primeiro espaço
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))