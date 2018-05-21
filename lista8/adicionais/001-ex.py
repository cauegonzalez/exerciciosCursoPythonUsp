def maior_elemento(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i;
    return maior

def test_maior():
    assert maior_elemento([1,2,3,4,5,6,7,8,9]) == 9
    assert maior_elemento([15,70,348,9]) == 348
    assert maior_elemento([1234,56,789]) == 1234
    assert maior_elemento([14,89]) == 89
    assert maior_elemento([123,2234,3245,42343,5432,6342,457,863,93]) == 42343
