def es_par(n):
    if n > 1:
        return es_par(n-2)
    elif n == 1:
        return False
    elif n == 0:
        return True
    return None


print('Es_par(0): {0}'.format(es_par(0)))
print('Es_par(1): {0}'.format(es_par(1)))
print('Es_par(2): {0}'.format(es_par(2)))
print('Es_par(3): {0}'.format(es_par(3)))
print('Es_par(4): {0}'.format(es_par(4)))
print('Es_par(10): {0}'.format(es_par(10)))
print('Es_par(111): {0}'.format(es_par(111)))