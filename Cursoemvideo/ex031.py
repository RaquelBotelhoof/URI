dis = float(input('Qual a distância em Km da sua viagem?'))
if dis <= 200:
    print('Valor da passagem será de {:.2f} reais'.format(dis*0.50))
else:
    print('Valor da passagem será de {:.2f} reais'.format(dis*0.45))
