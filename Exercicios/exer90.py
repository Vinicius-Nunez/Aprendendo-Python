ficha = list()
alunos = dict()
for c in range(0,3):
    alunos['Nome'] = str(input(f'Digite o nome do {c+1}º aluno: '))
    alunos['Nota1'] = float(input(f'Digite a 1º nota do aluno: '))
    alunos['Nota2'] = float(input(f'Digite a 2º nota do aluno: '))
    alunos['media'] = (alunos['Nota1']+ alunos['Nota2'])/2
    if alunos['media'] >= 7:
        alunos['Situacao']= '\033[42mAprovado\033[m'

    elif alunos['media'] < 7 and alunos['media'] >= 5.5:
        alunos['Situacao']= '\033[43mRecuperação\033[m'
    else:
        alunos['Situacao']='\033[41mReprovado\033[m'
    del alunos['Nota1']
    del alunos['Nota2']
    ficha.append(alunos.copy())
print('-='*20)
for e in ficha:
    for k, v in e.items():
        print(f'{k} é igual a: {v}')
    print()



