l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(l, a, area))
print('Considerando que é necessário 1l de tinta para cada 2m², você precisará de {:.2f}l de tinta'.format(area / 2))
