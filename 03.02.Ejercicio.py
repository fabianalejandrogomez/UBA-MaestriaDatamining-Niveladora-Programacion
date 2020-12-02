import sys


def factorial(n):
    out = 1
    while n > 0:
        out *= n
        n -= 1
    return out


def combinatorio(n,k):
    return factorial(n) / (factorial(k) * factorial(n-k))


def ejercicio_1():
    if len(sys.argv) > 1 and int(sys.argv[1]):
        base = int(sys.argv[1])
        print('{0}! = {1}'.format(base, factorial(base)))
    else:
        print('Debe ingresar un número')



def ejercicio_2():
    if len(sys.argv) > 2 and int(sys.argv[1]) and int(sys.argv[2]):
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        print('Fact(n): {0}, Fact(k): {1}, Fact(n-k): {2}'.format(factorial(n), factorial(k),factorial(n-k)))
        if n >= k:
            print('({0} C {1}) = {2}'.format(n, k, combinatorio(n,k) ))
        else:
            print('El primer parámetro tiene que ser mayor/igual que el segundo')
    else:
        print('Debe ingresar un número')


def ejercicio_3():
    if len(sys.argv) > 2 and int(sys.argv[1]) and int(sys.argv[2]):
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        if n >= k:
            i = k
            while i < n:
                print('({0} C {1}) = {2}'.format(n, i, combinatorio(n,i) ))
                i += 1
        else:
            print('El primer parámetro tiene que ser mayor/igual que el segundo')
    else:
        print('Debe ingresar un número')

ejercicio_3()