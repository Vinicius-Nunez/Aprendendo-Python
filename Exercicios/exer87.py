matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for i in range(0,3):
    for c in range(0,3):
        matriz[i][c] = int(input(f'Digite um valor [{i}:{c}]: '))
for i in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]:^5}]',end=' ')
        if matriz[i][c]%2 == 0:
            spar += matriz[i][c]

    print()
print('-='*30)
print(f'A soma dos valores pares deu {spar}')
for i in range(0,3):
    scol += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if matriz[1][c] > mai:
        mai = matriz[1][c]
    
print(f'E o maior valor da segunda linha é {mai}')
print('-='*30)




            
   
        
        