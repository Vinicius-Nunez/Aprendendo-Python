nome = str(input('digite seu nome: '))
if nome == 'vini':
    print('Eita nome bonito em!!')
elif nome == 'pedro' or nome == 'maria' or nome == 'joao':
    print('Seu nome é muito popular!')
elif nome in 'ana paula catalina victoria':
    print('belo nome feminino.')
else:
    print('seu nome é estranho')
print(f'tenha um bom dia {nome}')