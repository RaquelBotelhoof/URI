compra = input()
prazo = int(input())

if prazo == 0:
    print('chega hoje!')
else:
    if compra == 'domingo':
        entrega = 1 + prazo
    elif compra == 'segunda':
        entrega = 2 + prazo
    elif compra == 'terça':
        entrega = 3 + prazo
    elif compra == 'quarta':
        entrega = 4 + prazo
    elif compra == 'quinta':
        entrega = 5 + prazo
    elif compra == 'sexta':
        entrega = 6 + prazo
    else:
        entrega = 7 + prazo

    if entrega > 7:
        entrega -= 7

    if entrega == 1:
        print('sera entregue domingo')
    elif entrega == 2:
        print('sera entregue segunda')
    elif entrega == 3:
        print('sera entregue terca')
    elif entrega == 4:
        print('sera entregue quarta')
    elif entrega == 5:
        print('sera entregue quinta')
    elif entrega == 6:
        print('sera entregue sexta')
    else:
        print('sera entregue sabado')
