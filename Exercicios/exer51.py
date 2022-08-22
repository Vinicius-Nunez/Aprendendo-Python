comeco = int(input('digite o comeco: '))
pas = int(input('digite o termo: '))
temp = comeco + (10-1) * pas
for c in range(comeco, temp+1, pas):
    print(c, end=' -> ')