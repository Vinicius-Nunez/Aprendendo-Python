km = int(input('digite quantos km de viagem: '))
if km <=200:
    valor= km*0.50
    print(f'o valor da sua passagem é de RS{valor:.2f}')
else:
    valores = km * 0.45
    print(f'valor da sua passagem é de RS{valores:.2f}')
print('Tenha uma boa viagem!')