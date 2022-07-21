# Usa a função while, que só termina o laço quando M ou F for digitado

sexo = input('Informe o seu sexo [M/F]: ').upper()

while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper()

print('Sexo {} registrado com sucesso.'.format(sexo))