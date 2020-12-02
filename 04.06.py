def despedir(x):
    x.append('chau')
    print(len(x))

a = ['hola', 'mundo']
despedir(a)
print(a)
despedir(list(a))
print(a)

# Imprimir 3, lista con 3 elementos, 4, lista con 3 elementos
# El list(a) pasa una copia