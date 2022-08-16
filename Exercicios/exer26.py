frase = input('digite uma frase: ').strip().upper()
print('quantas letras A existem: ',frase.count('A'))
print('a primeira letra A aparece na posicao: ',frase.find('A')+1)
print('a ultima letra A aparece na posicao: ',frase.rfind('A')+1)