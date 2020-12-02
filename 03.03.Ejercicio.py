import sys


def ejercicio_1():
    if len(sys.argv) > 1 and int(sys.argv[1]):
        n = int(sys.argv[1])
        i = 0
        aux = ''
        while i < n:
            aux += '*'
            print(' ' + aux + '\t\t' + '*')
            i += 1
        i = 0
        print('\n')

        while i < n:
            print(' ' + aux)
            i += 1

    else:
        print('Debe ingresar un número')


ejercicio_1()