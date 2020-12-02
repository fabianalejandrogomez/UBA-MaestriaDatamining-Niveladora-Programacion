def mesetas(lista):
    valor = -1
    longitud = 0
    aux_valor = lista[0]
    aux_long = 1
    valor_ant = lista[0]
    i = 1
    while i < len(lista):
        print('i: {0}, lista[i]: {1}, valor: {2}, '
              'longitud: {3}, aux_valor: {4}, '
              'aux_long: {5}'.format(i, lista[i], valor, longitud, aux_valor, aux_long))
        if lista[i] == aux_valor:
            aux_long += 1
        else:
            if aux_long > longitud:
                longitud = aux_long
                valor = aux_valor
            aux_valor = lista[i]
            aux_long = 1
        i += 1
    return (valor, longitud)


input = [1, 1, 3, 6, 6, 6, 8, 8]
# input = [1, 1,3,6,6,6,6,8,8]
print(mesetas(input))
