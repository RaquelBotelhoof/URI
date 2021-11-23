def bissextos(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


inicio = int(input())
fim = int(input())
qtd_bissextos = 0

for ano in range(inicio, fim + 1):
    if bissextos(ano):
        print(ano)
        qtd_bissextos += 1
print(f'bissextos: {qtd_bissextos}')
