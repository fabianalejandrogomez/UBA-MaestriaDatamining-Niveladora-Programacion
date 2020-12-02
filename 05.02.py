# Para este ejercicio, adaptar los algoritmos de búsqueda vistos en clase.
# (a) Escribir un algoritmo que, dados una lista A y un entero x, retorne todos los elementos de
# A menores o iguales que x. Estimar el orden de complejidad temporal (en peor caso) del
# algoritmo.
# (b) Igual al punto anterior, pero sabiendo que la lista está ordenada.


def menores(lista, x):
    out = []
    for i in lista:
        if i <= x:
            # yield i
            out.append(i)
    return out


def menores_ordenados(lista, x):
    izq, der = 0, len(lista) - 1
    esta, pos = False, -1
    while izq < der:
        med = (izq + der) // 2
        print('izq: {0}, der: {1}, med: {2}'.format(izq, der, med))
        if lista[med] < x:
            izq = med + 1
        else:
            der = med

        # if len(lista) != 0 and x == lista[izq]:
        #     print('If true')
        #     esta, pos = True, izq

    # print('pos: {0}, lista[pos]: {1}'.format(pos, lista[pos]))
    print('pos: {0}, lista[pos]: {1}'.format(izq, lista[izq]))
    return lista[0:izq]


l = [1, 2, 7, 11, 52, 12, 5, 8, 4, 3, 21, 45, 38]
print(menores(l, 25)) # o(n)
print(menores_ordenados(sorted(l), 25)) # O(log n)
