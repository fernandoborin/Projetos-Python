# Lê os dados de 4 pessoas e fornece informações 

idadetotal = 0
mulheres = 0
idadeantiga = 0

for i in range(1,5):
    print('----- {}ª Pessoa -----'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    
    idadetotal += idade

    if sexo == 'M' and idade >= idadeantiga:
        idadehomem = idade
        nomehomem = nome
        idadeantiga = idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    

print('A média de idade do grupo é de {} anos'.format(float(idadetotal / i)))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehomem, nomehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
