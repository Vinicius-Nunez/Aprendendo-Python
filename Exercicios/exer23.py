num = int(input('Digite um valor: '))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print(f'analisando o numero {num}...')
print(f'A unidade é {u}')
print(f'A dezena é {d}')
print(f'A centena é {c}')
print(f'Milhar é {m}')