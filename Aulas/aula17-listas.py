lanche = ['bolo','pao','leite']

lanche.append('carne')#Adiciona maisum valor a lista
print(lanche)
lanche[2]= 'suco'#Substitui um valor especifico
print(lanche)
lanche.insert(0,'chocolate')#escolhe o vetor e adiciona um valor
print(lanche)
del lanche[3]#deleta um elemento especifico
'''lanche.pop()#deleta um elemento especifico escolhendo o vetor'''
'''lanche.remove('')#remove um valor especifico usando o nome do elemento.'''

valores = list(range(4,11,2))
print(valores)

valor = [8,5,4,7,6,3,1,9,2]
valor.sort()#deixa em ordem numerica/Alfabetica
print(valor)
valor.sort(reverse=True)#deixa em ordem reversa numerica\Alfabetica
print(valor)

for c, v in enumerate(valor):# O enumerate pega primeiro o vetor e depois o valor da lista.
    print(f'na posicao {c+1} temos o elemneto {v}..',)
toma = list()
for cont in range(0,5):
    toma.append(int(input('Digite um valor: ')))
for b, h in enumerate(toma):
    print(f'na posicao {b+1} temos o elemneto {h}..',)
a = [1,5,2,3,8]
b = a[:]# [:] signifca copiar os valor dentro da lista 'a'.
b[2]= 9
print(b)
print(a)