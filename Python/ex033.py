valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
valor3 = int(input('Terceiro valor: '))
"""valores = [valor1, valor2, valor3]
valores.sort()
print('O menor valor digitado foi {}'.format(valores[0]))
print('O maior valor digitado foi {}'.format(valores[-1]))"""
#Verificando o menor
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
#Verificando o maior
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
