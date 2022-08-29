totmulher20 = cont = conta = 0 
sexo = ' '
while True:
    print(f'---- CADASTRE UMA PESSOA ----')
    idade = int(input('Digite a sua idade: '))
    while sexo not in 'MF':
        sexo = input('Digite seu sexo [M\F]: ').upper().strip()
    if idade > 18:
        conta +=1
    if sexo == 'M':
        cont += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    continuar= ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar?:[S/N] ').upper()
    if continuar == 'N':
        break   
print(f'Total de pessoa com mais de 18 anos> {conta}')
print(f'Numeros de homens cadastrados: {cont}')
print(f'Total de mulheres com menos de 20 anos: {totmulher20}')