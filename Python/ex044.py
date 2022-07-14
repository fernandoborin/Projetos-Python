vi = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
opção = int(input("""[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? """))
if opção == 1:
   vf = vi * 0.9
elif opção == 2:
    vf = vi * 0.95
elif opção == 3:
    vf = vi
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(vf / 2))
elif opção == 4:
    vf = vi * 1.2
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, vf / parcelas))
else:
    vf = vi 
    print('Opção inválida, tente outra vez.')
print('Sua compra de R${:.2f} vai custar  R${:.2f} no final.'.format(vi, vf))