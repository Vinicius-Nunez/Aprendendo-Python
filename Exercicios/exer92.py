dados= {}
dados['nome']= str(input('Nome: '))
dados['ano']= int(input('Ano de Nascimento: '))
dados['ctps']= int(input('Carteira de Trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['idade'] = 2022-dados['ano']
    dados['contratacao']= int(input('Ano de Contratacao: '))
    dados['salario']= float(input('Salario: '))
    dados['aposentadoria'] = dados['contratacao']-dados['ano']+35 
    del dados['ano']
print('-='*15)
for k, c in dados.items():
    print(f'-{k} tem o valor {c}')
    

'''prev = {}
prev['nome'] = input('Nome: ')
prev['nascimento'] = int(input('Ano de nascimento: '))
prev['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if prev['ctps'] != 0:
    prev['idade'] = 2022 - prev['nascimento']
    prev['contratacao'] = int(input('Ano de contratação: '))
    prev['salario'] = float(input('Salario: R$'))
    prev['aposentadoria'] = prev['contratacao']-prev['nascimento'] + 35
for k,c in prev.items():
    print(f'{k} tem o valor {c}')'''