def cantidad_ocurrencias(n,l):
    if len(l) == 0:
        return 0
    else:
        return (1 if l[0] == n else 0) + cantidad_ocurrencias(n, l[1:])
# Inline if

print(cantidad_ocurrencias(1, [1,1,1,1,2,3,1,2,3,1]))
print(cantidad_ocurrencias(2, [1,1,1,1,2,3,1,2,3,1]))
print(cantidad_ocurrencias(3, [1,1,1,1,2,3,1,2,3,1]))
print(cantidad_ocurrencias(4, [1,1,1,1,2,3,1,2,3,1]))