def pot_dos(n):
    if n == 0:
        return 1
    else:
        return 2 * pot_dos(n - 1)


def pot_a(a, n):
    if n == 0:
        return 1
    else:
        return a * pot_a(a, n - 1)


print(pot_dos(2))
print(pot_dos(3))
print(pot_dos(4))
print(pot_dos(5))
print('')
print(pot_a(3,2))
print(pot_a(3,3))
print(pot_a(3,4))
print(pot_a(3,5))
