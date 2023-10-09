p = 11
q = 98
n = p * q


# DIVISORES DE N
def valid_n(n):
    divisores_n = list()
    for i in range(2, n):
        if n % i == 0:
            divisores_n.append(i)
        if len(divisores_n) == 2:
            valido = True
        else:
            valido = False
    return valido


print(valid_n(n))
