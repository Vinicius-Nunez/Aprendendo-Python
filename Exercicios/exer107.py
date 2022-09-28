from funcoes.numeros import dobro, metade, aumento, diminuir
from funcoes.linhas import lin


num = int(input('Digite um valor: '))
taxa = str(input('Qual a % da taxa ? '))
lin('Manipulando Dinheiro')
if taxa.isnumeric():
    taxa=int(taxa)
else:
    taxa=10


print(f'A metade de R${num} é R${metade(num):.2f}')
print(f'O dobro de R${num} é R${dobro(num):.2f}')
print(f'Aumentando %{taxa}, temos {aumento(num, taxa)}')
print(f'Diminuindo %{taxa}, temos {diminuir(num,taxa):.2f}')