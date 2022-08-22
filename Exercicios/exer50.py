soma = s =0
for c in range(0,6,1):
    valor = int(input('digite um valor: '))
    if valor % 2 ==0:
        soma += valor
        s += 1
print(f'a soma dos {s} valores pares deu o resultado {soma}')