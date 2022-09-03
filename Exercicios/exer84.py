lista = []
lista2 = []
conta = maior = menor = 0
nome = []
nome2 = []

while True:
    lista.append(str(input('Digite um nome: ')))
    lista.append(float(input('Digite o peso: ')))
    if len(lista2) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] >maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    cont = input('Quer continuar? [S/N]').upper().strip()[0]
    conta +=1
    lista2.append(lista[:])
    lista.clear()
    if cont =='N':
        break

    
print(f'O maior peso foi de {maior}', end=' ')
for p in lista2:
    if p[1] == maior:
        print(f'peso de {p[0]}', end=' ')
print(f'\nO menir peso foi de {menor} ')
for p in lista2:
    if p[1] == menor:
        print(f'peso de {p[0]}', end=' ')
print(f'\nVoce cadastrou {conta} pessoas')