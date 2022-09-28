from funcoes.NFormatos import dobro, metade, aumento, diminuir, moeda
from funcoes.linhas import lin


num = float(input('Digite um valor: '))
taxa = str(input('Qual a % da taxa ? '))
lin('Manipulando Dinheiro')
if taxa.isnumeric():
    taxa=int(taxa)
else:
    taxa=10


print(f'A metade de {moeda(num)} é R${metade(num, True)}')
print(f'O dobro de R${moeda(num)} é R${dobro(num, True)}')
print(f'Aumentando %{taxa}, temos {aumento(num, taxa, True)}')
print(f'Diminuindo %{taxa}, temos {diminuir(num,taxa, True)}')