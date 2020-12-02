import sys


def ejercicio_1():
    if len(sys.argv) > 2 and int(sys.argv[1]) and int(sys.argv[2]):
        base = int(sys.argv[1])
        exponente = int(sys.argv[2])

        i = 0
        aux = 1
        out_prod = 0
        out_exp = 1
        while i < exponente:
            j = 1
            while j < base:
                out_exp += aux
                j += 1
                # print('i: {0}, j: {1}, base: {2}, exponente: {3}, out_exp: {4}, aux: {5}'.format(i,j,base, exponente, out_exp, aux))

            out_prod += base
            aux = out_exp
            i += 1

        print('{0} * {1} = {2}'.format(base, exponente, out_prod))
        print('{0} ^ {1} = {2}'.format(base, exponente, out_exp))
    else:
        print('Debe ingresar un número')


ejercicio_1()