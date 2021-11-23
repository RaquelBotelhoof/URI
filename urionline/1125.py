trabalho = float(input())
prova = float(input())

media = float(trabalho + prova) / 2

if media >= 6.0:
    print('aprovado')
else:
    media = (trabalho + 10) / 2
    if media >= 6.0:
        print('talvez com a sub')
    else:
        print('reprovado')
