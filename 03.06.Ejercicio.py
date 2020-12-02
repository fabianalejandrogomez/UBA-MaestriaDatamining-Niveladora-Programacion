def reversar(cadena):
    out = ''
    i = len(cadena) - 1
    while i >= 0:
        out += cadena[i]
        i -= 1
    return out


print(reversar('Hola'))

print('Hola'[::-1])
print([x])