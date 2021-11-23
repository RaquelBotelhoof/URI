from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento com 4 dígitos (0000):'))
gen = str(input('Qual o seu gênero de nascimento? (M/F):')).strip().title()
idade = atual - nasc
if gen[0] == 'F':
    print('Para as pessoas cujo o gênero de nascimento é feminino, o alistamento militar não é obrigatório')

elif gen[0] == 'M':
    print(f'Voce nasceu em {nasc} tem {idade} anos em 2021.')
    if idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o seu alistamento.')
        print(f'Seu alistamento será em {atual + saldo}')

    elif idade > 18:
        saldo = idade - 18
        print(f'Já deveria ter se alistado há {saldo} anos.')
        print(f'Seu alistamento foi em {atual - saldo}')
    else:
        print('Deve se alistar imediatamente.')




