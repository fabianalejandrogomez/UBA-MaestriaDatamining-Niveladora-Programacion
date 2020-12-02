import sys


def ejercicio_2_1_a():
    for i in range(10):
        print('{0} {1}'.format(i * 10, round(i * 10 * 1.61, 2)))


def ejercicio_2_1_b():
    print('\t Mi \t Km')
    for i in range(10):
        print('\t {0} \t {1}'.format(i * 10, round(i * 10 * 1.61, 2)))


def ejercicio_2_1_c():
    print('\t Km \t Mi')
    for i in range(10):
        print('\t {0} \t {1}'.format(i * 10, round((i * 10) / 1.61, 2)))


def ejercicio_2_2_a():
    # print(sys.argv[1])
    if len(sys.argv) > 1:
        if int(sys.argv[1]):
            for i in range(int(sys.argv[1])):
                print(i + 1)
        else:
            print('Debe ingresar un número')
    else:
        print('Debe ingresar un número')


def ejercicio_2_2_b():
    if len(sys.argv) > 1 and int(sys.argv[1]):
        for i in range(int(sys.argv[1])):
            if i % 2 == 1:
                print(i)
    else:
        print('Debe ingresar un número')


def ejercicio_2_3_a():
    if len(sys.argv) > 1 and int(sys.argv[1]):
        print('\n', end=' ')
        for i in range(int(sys.argv[1])):
            for j in range(i + 1):
                print(' *', end=' ')
            print('\n', end=' ')
    else:
        print('Debe ingresar un número')


def ejercicio_2_4():
    if len(sys.argv) > 1 and int(sys.argv[1]) + 1:
        print('\n', end=' ')
        i = 1
        while i < (int(sys.argv[1]) + 1):
            print('\t n = {0}'.format(i))
            fact = 1
            sumatoria = 0
            sum_1_t = 0
            j = 1
            while j <= i:
                fact *= j
                sumatoria += j
                sum_1_t += 1 / j
                j += 1

            print('\t\t a) n!= {0}'.format(round(fact, 4)))
            print('\t\t b) 1/n!= {0}'.format(round(1 / fact, 4)))
            print('\t\t c) sumatoria = {0}'.format(round(sumatoria, 4)))
            print('\t\t c) sum(1/t) = {0}'.format(round(sum_1_t, 4)))
            i += 1
    else:
        print('Debe ingresar un número')


primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def ejercicio_2_5():
    if len(sys.argv) > 1 and int(sys.argv[1]):
        valor_control = int(sys.argv[1])
        if valor_control in primos:
            return True
        print('\n', end=' ')
        index = 0
        # print('Inicio \n')
        # print('Index: {0}. Len: {1}. Valor_control: {2}. Primo_index: {3}'.format(index, len(primos), valor_control, primos[index]))
        while index < len(primos) and valor_control >= primos[index]:
            print('Primo: {0}'.format(primos[index]))
            if valor_control % primos[index] == 0:
                return False
            index += 1
        return True
    else:
        print('Debe ingresar un número')


print(ejercicio_2_5())
