print('-'*30)
print('{:^30}' .format(' BANCO NARUTO USMK '))
print('-'*30)
sacar = int(input('Qual valor você quer sacar? R$'))
cinquenta = vinte = dez = um = cem = 0
while True:
    while sacar - 100 >=0:
        sacar -= 100
        cem +=1
    while sacar - 50 >= 0:
        sacar -= 50
        cinquenta += 1
    while sacar - 20 >= 0:
        sacar -= 20
        vinte += 1
    while sacar - 10 >= 0:
        sacar -= 10
        dez += 1
    while sacar - 1 >= 0:
        sacar -= 1
        um += 1
    break
if cem != 0:
    print(f'Total de {cem} cedulas de R$100')
if cinquenta != 0:
    print(f'Total de {cinquenta} cedulas de R$50')
if vinte != 0:
    print(f'Total de {vinte} cedulas de R$20')
if dez != 0:
    print(f'Total de {dez} cedulas de R$10')
if um != 0:
    print(f'Total de {um} cedulas de R$1')