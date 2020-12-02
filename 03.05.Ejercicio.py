
def Palindromo(cadena):
    aux = len(cadena) - 1
    i = 0
    while i < aux / 2:
        print('i: {0}, cadena[i]: {1}, aux: {2}, cadena[aux-i]: {3}'.format(i, cadena[i], aux, cadena[aux-i]))
        if cadena[i] != cadena[aux-i]:
            return False
        i += 1
    return True

print(Palindromo('anilina'))
print(Palindromo('hola'))