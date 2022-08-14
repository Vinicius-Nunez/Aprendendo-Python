km=float(input('digite o valor de kms rodados: '))
dia=int(input('digite quantos dias ficou com o carro: '))
res= km*0.15
res2=dia*60
resultado=res+res2
print(f'voce rodou {km}km e ficou com o carro por {dia} dias, o valor total a ser pago é de RS{resultado}')