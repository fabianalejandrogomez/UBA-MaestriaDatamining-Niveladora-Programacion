def productoria(lista):
    if len(lista) == 0:
        return 1
    else:
        return lista[0] * productoria(lista[1:])


print(productoria([4,2,3]))