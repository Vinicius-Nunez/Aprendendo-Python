tot = maior = menor = contador = lol= 0
prod = ' '
print('-'*30)
print('LOJÃO DO JOÃO, COMPRE BARATÃO')
print('-'*30)
while True:
    nome= str(input('Digite o nome do produto: ').upper().strip())
    preco= float(input('Digite o valor do produto: ').strip())
    tot+= preco
    lol += 1
    if preco > 1000:
        contador += 1

    if lol== 1 or preco < menor:
        menor = preco
        prod = nome  
        
    cont= ' '
    while cont not in 'SN':
        cont = input('Quer continuar?[S/N] ').upper().strip()[0]
    if cont == 'N':
        break
print(f'A soma de todos os produtos deu o total de: RS{tot:.2f}')
print(f'Temos {contador} produtos que custam mais de RS1000 reais')
print(f'O produto mais barato foi {prod} e custou {menor:.2f} ')   