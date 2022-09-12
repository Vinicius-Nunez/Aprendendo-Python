def lin():
    print('-='*25)

lin()
print('corno')
lin()
print('corno')
lin()
print('corno')
lin()
print('corno')
lin()

def total(txt):
    print('='*len(txt))
    print(f'{txt}')
    print('='*len(txt))

total('gustavo corno')

lin()

def soma(a, b):
    s = a+b
    print(f'A soma de {a}+{b} = {s} ')
soma(4,6)

lin()

def contador(*num):
    print(sum(num))
contador(4, 5, 6, 8, 3, 1)

lin()


valores=[6, 2, 3, 5, 7, 8]
def dobra(list):
    pos =0
    while pos < len(list):
        list[pos] *=2
        pos +=1
dobra(valores)
print(valores)

lin()

valores = []
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
for c in range(0,4):
    valores.append(int(input('Num: ')))
dobra(valores)
print(valores)