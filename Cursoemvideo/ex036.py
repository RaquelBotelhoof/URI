casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
minimo = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NÃO pode ser CONCEDIDO, pois o valor da parcela passa de 30% do seu salário')
