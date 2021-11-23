nome = str(input('Qual o seu nome?'))
if nome =='Raquel':
    print('Que nome bonito!')
elif nome =='Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Você tem um nome popular no Brasil')
elif nome in 'Ana, Cláudia, Jéssica, Juliana':
    print('Voce tem um belo nome feminino')
print('Tenha um bom dia, {}!'.format(nome))
