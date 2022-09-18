def resp(*n, sit=False):
    """_Pega os valor adicionados e mostra qual foi o maior, menor e a media._

    Args:
        sit (bool, optional): _opcao para mostrar a situacao do aluno_. Defaults to False.

    Returns:
        _type_: _retorna o valor do dicionario._
    """
    notas = {}
    notas['total']= len(n)
    notas['maior']= max(n)
    notas['menor']= min(n)
    notas['media'] = sum(n)/len(n)
    if sit:
        if notas['media'] >=7:
            notas['situacao']='BOA'
        elif notas['media'] >=5:
            notas['situacao']='razoavel'
        else:
            notas['situacao']='ruim'

    return notas
    
res = resp(5.5,2,5.3, sit=True)
print(res)
help(resp)