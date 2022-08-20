preco = float(input('Digite o valor a serpago no produto: '))
print(' [1]- A vista dinheiro com 10% de desconto\n [2]- A vista cartao de credito com 5% de desconto\n [3]- Parcelado em 2x sem juros\n [4]- parcelado em 3x ou mais com 20% de juros.')
opcao = int(input('Selecione a forma de pagamento a cima! '))
if opcao == 1:
    print(f' O valor do produto é {preco} e com o disconto de 10% ficara {preco - preco * 0.10:.2f} Reais')
elif opcao == 2:
    print(f' O valor do produto é {preco} e com disconto de 5% ficara {preco - preco * 0.05:.2f} Reais')
elif opcao == 3:
    print(f'O valor do produto ficara no valor de {preco:.2f}')
else:
    print(f' O valor do produto é {preco} e com o juros de 20% ficara no valor total de {preco + preco * 0.20:.2f}')