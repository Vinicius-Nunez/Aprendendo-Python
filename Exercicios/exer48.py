cont= s = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        cont += 1
        s += c

print(f'A soma de todos os {cont} valores solicitados é {s}')