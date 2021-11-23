def eh_primo(n):
    num_divisores = 0  # conta o número de divisores de n
    candidato = 1  # número candidato a divisor
    while candidato <= n:
        if n % candidato == 0:  # testa se n é divisível por candidato
            num_divisores += 1
        candidato += 1
    if num_divisores == 2:  # testa se o número de divisores de n é igual a 2 (se for, é primo)
        return True
    else:
        return False


def lista_primos(n):
    primos_encontrados = []  # começa como uma lista vazia
    for i in range(2, n):  # varia i de 2 até n-1
        if eh_primo(i):
            primos_encontrados.append(i)
    return primos_encontrados  # devolve (retorna) a lista no final
