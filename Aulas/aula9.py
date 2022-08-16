frase= 'tudo e mais um pouco'
print(frase.count('u'))#mostra quantas vezes a letra indicada aparece na frase.
print(len(frase))#conta o tamnho da palavra.
print(frase.find('pou'))#acha a palavra indicada e diz em qual posicao ela comeca.
print('mais' in frase)#diz se a palavra indicada existe na frase.
print(frase.replace('u','y'))#faz a subistituicao de uma palavra.
print(frase.upper())#faz tudo ficar em maiuscula.
print(frase.lower())#faz tudo ficar em minusculo.
print(frase.capitalize())#deixa tudo em minusculo exeto a primeira letra da primeira palavra.
print(frase.title())#deixa todas a letras das palavras em maiuscula.
print(frase.strip())#remove todos os espacos inulteis no comeco e no fim.
print(frase.rstrip())#remove os espacos inulteis do fim.
print(frase.lstrip())#remove os espacos inulteis do comeco.
print(frase.split())#faz uma divisao em todos os espacos entre as palavras.
print('-'.join(frase))#junta as strings com simbolos ou tracos.

