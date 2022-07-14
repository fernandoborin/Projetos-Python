import math
ang = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(ang)
print('O ângulo de {}º tem o SENO igual a {:.2f}'.format(ang, math.sin(rad)))
print('O ângulo de {} tem o COSSENO igual a {:.2f}'.format(ang, math.cos(rad)))
print('O ângulo de {} tem a TANGENTE igual a {:.2f}'.format(ang, math.tan(rad)))
