from datetime import date
idade = int(input('Digite seu ano de nascimento: '))
ano = date.today().year-idade
print(f'sua idade é {ano}')
if ano <= 9:
    print('categoria Mirim')
elif ano <=14:
    print('categoria Infantil!')
elif ano <=19:
    print('categoria Junior!')
elif ano == 20:
    print('categoria Senior!')
else:
    print('categoria Master!!')