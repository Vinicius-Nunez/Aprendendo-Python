valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor, na posicao {cont}: ')))
maior = max(valores)
menor = min(valores)
print(f'voce digitou os valores {valores}')
print(f'O maior valor é {maior} e esta na posicao ', end=' ')
for i, c in enumerate(valores):
    if c == maior:
        print(f'{i}..', end='')

print(f'\nO menor valor foi {menor} e esta na posicao ', end=' ')
for i, c in enumerate(valores):
    if c == menor:
        print(f'{i}..', end='')