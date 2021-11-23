v = int(input('Digite a velocidade do carro: '))
if v<=80:
   print('Dirija com segurança. Boa viagem.')
else:
    print('Você foi multado por exeder o limite de 80km/h.')
    m = (v - 80) * 7
    print('A multa vai custar {:.2f} reais'.format(m))