a = 1
b = a
a = 2
print(b)

# Devuelve 1. Porq? Porque los tipos primitivos se pasan por copia y no por referencia.
####
# Tradicionalmente:
# Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
# Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...
# 
# Ref: https://docs.hektorprofe.net/python/programacion-de-funciones/paso-por-valor-y-referencia/
####
