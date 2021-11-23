from math import hypot
cto = float(input('Digite o cumprimento do cateto oposto:'))
cta = float(input('Digite o cumprimento do cateto adjacente:'))
hp = hypot(cto, cta)
print('A hipotenusa vai medir: {:.2f}'.format(hp))