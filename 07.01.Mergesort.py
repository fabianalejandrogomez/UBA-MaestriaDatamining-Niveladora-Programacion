def mergesort(lista):
    if len(lista) == 1
        return lista
    else:
        return mergesort(lista[0:len(lista)//2], lista[(len(lista) // 2) + 1:])