#name error -> sintaxe
#value error -> erro de valor int() -> str()
#zero division error -> divisão por 0 =!
#type error -> str -> int
#index error -> lst fora de range
#moduleNotfound -> modulo nao encontrado
#key error -> erro de chave
#keyboardInterrupt -> usuario para o programa
#memoryError -> erro de variavel
#connection error -> 
#runtime error -> erro de run

try:
    a = int(input('Digite o valor: '))
    b = int(input('Digite um valor: '))
    c = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('nao é possivel dividir um numero zero!')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados. ')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}, {erro}')
# except Exception as erro:
#     print(f'Problema encontrado foi {erro},{erro.__class__} :')# Para mostrar aonde esta o erro, apenas coloque a variavel 'Erro'
    
else:
    print(c)
finally:
    print('Volte sempre')