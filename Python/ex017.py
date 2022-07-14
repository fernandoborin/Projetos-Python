from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa do triângulo de cateto oposto {} e cateto adjacente {} é igual a {:.2f}'.format(ca, ca, hypot(co,ca)))