def cant_letras(listas):
    out = 0
    for i in listas:
        out += len(i)
    return out

parametro = ['hola', 'como', 'estas', 'bien', 'vos', 'muy bien', 'gracias']
print(cant_letras(parametro))
print(sum([len(x) for x in parametro]))


