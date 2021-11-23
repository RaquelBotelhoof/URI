from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento com 4 digitos (0000):'))
idade = atual - nasc

if idade <= 9:
    print('MIRIM')
elif idade < 15:
    print(' INFANTIL')
elif idade < 20:
    print(' JÚNIOR')
elif idade < 26:
    print('SÊNIOR')
elif idade > 25:
    print('MASTE')
