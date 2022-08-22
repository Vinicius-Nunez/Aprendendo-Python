
palavra = str(input('Digite uma palavra: ').strip().upper())
frase = palavra.split()
junto = ''.join(frase)
iverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    iverso += junto[letra]'''
if junto == iverso:
    print(f'A valavra {palavra} ivertidade é {iverso}')
    print('É palindromo ')
else:
    print('Nao é palindromo ')