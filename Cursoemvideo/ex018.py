from math import (radians, sin, cos, tan)
angulo = float(input('Digite um angulo qualquer:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {} tem seu seno de {:.2f}, seu cosseno {:.2f} e sua tangente {:.2f}.'.format(angulo, seno, cosseno, tangente))