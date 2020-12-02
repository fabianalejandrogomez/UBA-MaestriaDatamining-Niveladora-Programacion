def media(lista):
    out = 0
    for i in lista:
        out += i
    return out / len(lista)


def insertion_sort(lista):
    i = 0
    while i < len(lista):
        j = i
        while j > 0 and lista[j - 1] > lista[j]:
            lista[j - 1], lista[j] = lista[j], lista[j - 1]
            j -= 1

        i += 1


def mediana(lista):
    insertion_sort(lista)
    print('Lista: {0}, len(lista): {1}, long: {2}'.format(lista, len(lista), len(lista) - 1))
    long = len(lista)
    if long % 2 == 1:
        return lista[(long // 2)]
    else:
        return (lista[(long // 2) - 1] + lista[(long // 2)]) / 2


def es_primo(n):
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    i = 0
    while i > 0 and primos[i] < sqrt(n):
        if n % primos[i] == 0:
            return False
        i += 1
    return True


def decimal_a_binario(n):
    out = ''
    while n > 0:
        out = str(n % 2) + out
        n = n // 2
    return out


def binario_a_decimal(n):
    out = 0
    ult_pos = len(n) - 1
    print(ult_pos)
    for i in range(len(n)):
        # print('i: {0}, out: {1}, n[i]: {2}, '
        #       'ult_pos: {3}, 2^(ult_pos-i): {4}'
        #       .format(i, out, n[i], ult_pos, 2**(ult_pos-i)))
        out += int(n[i]) * 2 ** (ult_pos - i)
    return out


print(media([1, 2, 4, 6, 25, 367, 4, 21])) # Si
print(mediana([1, 2, 4, 6, 367, 4, 21]))
print(mediana([1, 2, 4, 6, 21, 367, 4, 21]))
print(es_primo(11)) # Si
print(decimal_a_binario(10)) # Si
print(binario_a_decimal('1111')) # si
