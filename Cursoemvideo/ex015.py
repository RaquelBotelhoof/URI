d = int(input('Quantos dias alugados?'))
km = float(input('Quantos kms rodados?'))
v = (d * 60) + (km * 0.15)
print(f'O total a apagar é de R${v:.2f}')
