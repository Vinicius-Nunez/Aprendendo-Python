def votacao(ano):
    idade= 2022-ano
    if idade <=15:
        print(f'Com a idade de {idade}, o voto nao é Obrigatorio!')
    elif idade <=17 or idade >=65:
        print(f'Com a idade de {idade}, o voto é Opcional! ')
    elif idade >=18 and idade <=64:
        print(f'Com a idade de {idade}, o voto é Obrigatorio! ')

n= int(input('Digite seu ano de nascimento: '))
votacao(n)

