a = [1,2]
b = a
a.append(3)
print(len(b))

# Porque las listas si se pasan por referencia, entonces ambas apuntan al mismo lugar. Da 3.