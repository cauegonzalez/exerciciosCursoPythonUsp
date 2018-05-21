def remove_repetidos(lista):
    lista.sort()
    tamanho = len(lista) - 1
    listaRetornada = []
    for i in lista:
        if (i not in listaRetornada):
            listaRetornada.append(i)
    return listaRetornada

def test_remocao():
    assert remove_repetidos([1,2,5,3,1,4,2]) == [1,2,3,4,5]
    assert remove_repetidos([1,2,5,3,1,4,2]*2) == [1,2,3,4,5]
    assert remove_repetidos([1,2,2,2,2,2,7,5,1,4,2]) == [1,2,4,5,7]
