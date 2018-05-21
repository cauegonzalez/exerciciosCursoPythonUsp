def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = soma + i

    return soma

def test_soma():
    assert soma_elementos([1,2,3]) == 6
    assert soma_elementos([1,2,3,1,2,3]) == 12
    assert soma_elementos([1,2,3,4,5,6]) == 21