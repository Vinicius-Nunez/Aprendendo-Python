
somaidade = mediaidade = maioridadehomem = totmulher20 = 0 
nomevelho = ''
for p in range(1, 5):
    print(f'    -----={p}º=-----')
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite seu sexo [M\F]: ').upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f' A media de idade do grupo é {mediaidade} anos')
print(f' O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f' Ao todo sao {totmulher20} mulheres com menos de 20 anos')