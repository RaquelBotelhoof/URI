nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#print('Seu primeiro nome é {} e ele tem {} letras'.format(sepra[0], len(separa[0])))

