num1 = 0
cont = 0
con = 0
num1 = int(input('digite um valor: '))
while num1 != 999:
    con += 1
    cont += num1
    num1 = int(input('digite um valor: '))

print(f'A soma de {con} valores é {cont}')

