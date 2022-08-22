from datetime import date
tot = 0
tott = 0
for c in range(1,8):
    ano = float(input(f'Digite o ano de nascimento da {c} pessoa: '))
    idade = date.today().year - ano
    if idade <18:
        tot +=1
    elif idade > 18:
        tott += 1      
print(f' Existe {tot} pessoas menores de 18 anos ')
print(f'existe {tott} pessoas maiores de 18 anos ')