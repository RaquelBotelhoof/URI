n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota'))
media = (n1+n2)/2
if media <5.0:
    print('REPROVADO')
elif media > 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
