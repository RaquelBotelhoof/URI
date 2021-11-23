from datetime import date
atual = date.today().year
nome = str(input('Digite seu nome: ')).strip().title().split()
ano_Nasc = int(input(f'{nome[0]}, digite o ano de seu nascimento com 4 dígitos (0000): '))
if ano_Nasc < 100: # caso o usuário digite o ano com apenas dois dígitos (se vc conhecer um jeito mais fácil de fazer me avise)
    aux = (atual // 100 % 100) * 100
    if atual - aux > ano_Nasc: # caso o ano digitado seja do século atual
        ano_Nasc += aux
    else: # caso seja do século anterior
        ano_Nasc += aux - 100
idade = atual - ano_Nasc
gen = str(input(f'{nome[0]}, qual o seu gênero nascimento? (M/F) ')).strip().title()
if gen[0] == 'F': #caso seja digitado "feminino"
    form_trat = 'Srta.'
    gen_art = 'a'
    print(f'{form_trat} {nome[0]}, para as pessoas cujo o gênero de nascimento é feminino, o alistamento militar')
    resp = str(input(f'é facultativo, {gen_art} {form_trat} deseja se alistar? (S/N) ')).strip().title()
    if resp[0] == 'S': # caso seja digitado "sim"
        alista_F = True
    else:
        alista_F = False
        print(f'{form_trat} {nome[0]}, obrigado por comparecer a esta junta Militar, tenha um ótimo dia!')
if gen[0] == 'M' or alista_F == True:
    if gen[0] == 'M': # caso seja digitado "masculino"
        form_trat = 'Sr.'
        gen_art = 'o'
    plural = 'anos' if idade > 1 else 'ano'
    print(f'{form_trat} {nome[0]}, neste ano de {atual}, {gen_art} {form_trat.lower()} terá completado {idade} {plural} de idade.')
    if idade < 18:
        dif = 18 - idade
        plural = f'faltam {dif} anos' if dif != 1 else 'falta 1 ano'
        print(f'{form_trat} {nome[0]}, ainda {plural} para o seu alistamento, nos procure novamente no ano de {atual + dif}')
    elif idade == 18:
        print(f'{form_trat} {nome[0]} neste ano de {atual}, '
              f'é o ano que {gen_art} {form_trat.lower()} deve fazer o seu alistamento militar')
    else:
        dif = idade - 18
        plural = f'{dif} anos' if dif != 1 else '1 ano'
        print(f'{form_trat} {nome[0]}, o seu alistamento deveria ter ocorrido no ano de {atual - dif} ou seja à {plural} atrás')
