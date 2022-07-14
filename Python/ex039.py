nasc = int(input('Ano de nascimento: '))
idade = 2021 - nasc
if idade == 18:
    print('Quem nasceu em {} tem {} anos em 2021'.format(nasc, idade))
    print('Você tem que se alistar imediatamente!')
elif idade > 18:
    print('Quem nasceu em {} tem {} anos em 2021'.format(nasc, idade))
    print('Você já deveria ter se alistado há {} ano(s)!'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(nasc + 18))
elif 1 <= idade < 18:
    print('Quem nasceu em {} tem {} anos em 2021'.format(nasc, idade))
    print('Ainda faltam {} ano(s) para o seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format(nasc + 18))
else:
    print('Idade inválida. Você é um viajante do tempo?')

#Poderia importar date de datetime
#from datetime import date
#Pro script usar a data do sistema