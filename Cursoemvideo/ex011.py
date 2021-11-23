l = float(input('Qual a largura da parede em metros?'))
a = float(input('Qual a altura da parede em metros?'))
p = l*a
print('Sua parede tem a dimensão de {}x{}, sendo assim sua area é de {:.2f}'.format(l, a, p))
t = p/2
print('Para pintar essa parede voce vai precisar de {:.2f} litros de tinta.'.format(t))
