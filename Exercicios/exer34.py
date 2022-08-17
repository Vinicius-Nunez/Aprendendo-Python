salario = float(input('digite o valor do seu salario: '))
if salario >= 1.250:
    aumento = salario * 0.10
    print(f'seu salario com o aumento de 10% foi de RS{salario+aumento:.3f}')
else:
    aumento = salario * 0.15
    print(f'seu salario com o aumento de 15% foi de RS{salario+aumento:.3f}')