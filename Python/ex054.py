# Identifica quantas pessoas são maiores e menores de idade usando for

from datetime import date

maiores = 0
menores = 0

for pessoa in range(1, 8):
    nascimento = int(input(('Em que ano a {}ª nasceu? '.format(pessoa))))
    if date.today().year - nascimento >= 18: # Detecta o ano atual do sistema
         maiores += 1
    else:
        menores += 1


print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('Ao todo tivemos {} pessoas menores de idade'.format(menores))