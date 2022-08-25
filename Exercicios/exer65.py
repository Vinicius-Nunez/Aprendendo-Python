menor= conta = media = maior = num = soma = 0
per = ' '
while per not in 'Nn':
    num = int(input('Digite um numero: '))
    per = str(input('Quer continuar [S/N]? '))
    conta += 1
    soma += num

    if conta == 1:
        maior = menor = num

    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    if per == 'Ss':
        num = int(input('Digite um numero: '))
    
media = soma / conta  
print(f'Voce digitou {conta} numeros e a media foi {media}', end='')
print(f'O maior valor foi {maior} e o menor foi {menor}')