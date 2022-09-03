'''matriz = [[],[],[]]
for c in range(0,9):
    num = int(input('Numero: '))
    if len(matriz[0]) < 3:
        matriz[0].append(num)
        matriz[0].copy()
    elif len(matriz[1]) < 3:
        matriz[1].append(num)
        matriz[1].copy()
    elif len(matriz[2]) < 3:
        matriz[2].append(num)
        matriz[2].copy()
for c in matriz[0]:
    print(f'[{c}]', end='\n ')
    
for i in matriz[1]:
    print(f'[{i}]',end='\n ')
    
for e in matriz[2]:
    print(f'[{e}]', end=' ')'''


matriz = [[0,0,0] ,[0,0,0] ,[0,0,0]]
for l in range(0,3):
    for i in range(0,3):
        matriz[l][i]= int(input(f'Digite um valor para [{l}, {i}]: '))
for l in range(0,3):
    for i in range(0,3):
        print(f'[{matriz[l][i]:^5}]', end=' ')
    print()