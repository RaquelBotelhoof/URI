salário = float(input('Qual é o seu salario?'))
if salário <= 1250:
    novo = salário + (salário *15 /100)
else:
    novo = salário + (salário *10 /100)
print('Quem ganahva R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salário, novo))
