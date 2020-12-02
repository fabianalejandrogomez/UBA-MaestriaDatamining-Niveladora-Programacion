def getMin(lista):
    output = 100000000000000
    for i in lista:
        if i < output:
            output = i
    return output


def getMax(lista):
    output = 0
    for i in lista:
        if i > output:
            output = i
    return output


def computeMean(lista):
    output = 0
    contador = 0
    for i in lista:
        output += i
        contador += 1

    return output / contador


def allTogether(lista):
    mean = 0
    count = 0
    min = 100000000000000
    max = 0
    for i in lista:
        if i < min:
            min = i
        elif i > max:
            max = i
        mean += i
        count += 1

    print('\n')
    print("El minimo valor es: ", min)
    print("El maximo valor es: ", max)
    print("El promedio es: ", mean / count)


valores = [23, 4, 67, 32, 13]
print("El minimo valor es: ", getMin(valores))
print("El maximo valor es: ", getMax(valores))
print("El promedio es: ", computeMean(valores))
allTogether(valores)
