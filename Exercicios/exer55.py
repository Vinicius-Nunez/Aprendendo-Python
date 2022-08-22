lista= []
for c in range(1,6):
    peso = float(input('Digite o peso da pessoa: '))
    lista.append(peso)#adiciona um numero a uma lista
print(f' o maior peso da lista é {max(lista)}')
print(f' O menor peso da lista é {min(lista)}')