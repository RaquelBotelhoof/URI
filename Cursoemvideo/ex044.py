print(f'{"Lojas Gunabara":=^40}')
prod = float(input('Qual o valor das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('''[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
formas = int(input('Digite à opção escolhida:'))
if formas == 1:
    pag = prod - prod * 0.10
elif formas == 2:
    pag = prod - prod * 0.05
elif formas == 3:
    pag = prod / 2
    print(f'Sua compra parcelada em 2x vai custar R${pag} sem juros.')
elif formas == 4:
    parcelas = int(input('Quantas parcelas?'))
    pag = prod * 0.2 + prod
    mes = pag / parcelas
    print(f'Sua compra parcelada em {parcelas}x vai custar {mes} com juros.')
else:
    pag = prod
    print('OPÇÃO INVALIDA de pagamento. Tente de novamente')
print(f'Sua compra de R${prod} vai custar R${pag} no total.')
