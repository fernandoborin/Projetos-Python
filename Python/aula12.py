nome = str(input('Qual é o seu nome? '))
if nome == 'Fernando':
    print('Que nome bonito rs')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('{}, que nome broxa kkkkkkk'.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Cuiékkkkkkkkkk')
else:
    print('Dia, apenas.')
print('Olá, {}!'.format(nome))
