nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if média >= 7:
    print('O aluno está APROVADO')
elif 5 <= média < 7:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está REPROVADO')

