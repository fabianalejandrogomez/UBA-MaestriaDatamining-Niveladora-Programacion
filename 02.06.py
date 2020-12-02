from math import sqrt


def es_perfecto(n):
    acum_divisores = 1
    i = 2
    while i < int(sqrt(n))+ 1:
        if n % i == 0:
            acum_divisores += i + n // i
        i += 1
    # print('n: {0}, divisores: {1}'.format(n, divisores))
    return n == acum_divisores


for i in range(2,10000):
    if es_perfecto(i):
        print('es_perfecto({0}) -> {1}'.format(i, True))
