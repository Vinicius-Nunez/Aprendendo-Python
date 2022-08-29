num1 = 0
cont = 0
con = 0
while True:
    num1 = int(input('digite um valor: '))
    if num1 == 999:
        break
    con += 1
    cont += num1
print(f'A soma de {con} valores é {cont}')