casa = float(input('digite o valor da casa: '))
salario= float(input('digite o seu salario: '))
tempo= int(input('tempo a pagar em anos: '))
anos= tempo * 12
prestacao= casa/ anos
if prestacao > salario*0.30:
    print('\033[0;35;41m Solicitacao negada!\033[m a prestacao por mes exedeu o limite de 30{%} o seu salario.')
else:
    print(f'\033[1;42mSolicitacao aprovada\033[m,Parabens!!')
