valor= int(input('digite um valor: '))
valor2= int(input('Digite outro valor: '))
if valor > valor2:
    print(f'O primeiro valor de {valor} é maior!')
elif valor2 > valor:
    print(f'O segundo valor de {valor2} é maior!')
else:
    print(f' os valores sao iguais {valor} = {valor2}')
